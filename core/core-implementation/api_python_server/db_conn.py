""" Module db_conn

    Created on 13/06/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""

# Import system libraries
from typing import Optional
import uuid
from datetime import datetime
import csv

# Import public libraries
from sqlalchemy import Column, DateTime, BigInteger
from sqlalchemy.exc import IntegrityError
from sqlmodel import Field, SQLModel, Session, Relationship, create_engine, select, sess


# Import application modules


class Client(SQLModel, table=True):
    """ The table collects metadata about clients. The metadata indicates:
        - the name of the client;
        - the email address of the client;
        - the phone number of the client;
        - the UUID used by the CRUD API to identify the client.
        - the UUID of the default scenario associated with the client, which is used for live updates
           and for data extractions using the legacy /data/ranges API endpoint.
        - the date and time when the client was created.
        - the list of subscriptions associated with the client (free form, to be refined later).
        - a one-to-many relationship with the Scenario table, which allows to retrieve the list of scenarios
          associated with a client.
        - a maximum number of scenarios that can be associated with a given client.
    """
    __tablename__ = "client"
    __table_args__ = {'schema': 'public'}
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    email: Optional[str]
    phone: Optional[str]
    uuid: Optional[str] = Field(default=None, index=True)  # UUID
    default_scenario: Optional[str]  # UUID
    since: datetime = Field(default_factory=datetime.now, sa_column=Column(DateTime(timezone=True)))
    subscriptions: Optional[str]
    max_scenarios: int = Field(default=1)
    
    scenarios: list["Scenario"] = Relationship(back_populates="client")


# class AreaScale(Enum):
#     """ The AreaScale enumeration defines the possible scales for geographic area.
#     """
#     WorldRegion = auto()
#     Continent = auto()
#     Country = auto()
#     State = auto()
#     Region = auto()
#     County = auto()
#     City = auto()
#     Location = auto()
#     Unit = auto()


# class Area(SQLModel, table=True):
#     """ The table collects metadata about areas. Areas are ordered in a hierarchy, with a parent-child
#         relationship defined by the optional parent/children relationship.
#         The metadata indicates:
#         - the name of the area;
#         - the type among "World Region", "Continent", "Country", "State", "Region", "County", "City", "Location", "Unit"
#           A street address corresponds to a Location. Units are subdivisions of Locations that may not have distinct
#           street addresses. Locations and units can have AreaDetail linked information with the street address, the
#           geographics coordinates and altitude, type of place, and other details.
#         - the children areas, if any; and
#         - the parent area, if any; and
#     """
#     __tablename__ = "area"
#     id: Optional[int] = Field(default=None, primary_key=True, index=True)
#     name: str
#     scale: AreaScale = Field(default=AreaScale.Location)
#     parent: Optional["Area"] = Relationship(
#         sa_relationship_kwargs={"remote_side": "Area.id", "cascade": "null"},
#         back_populates="children",
#     )
#     children: list["Area"] = Relationship(back_populates="parent")


class Scenario(SQLModel, table=True):
    """ The table collects metadata about scenarios. The metadata indicates:
        - if the scenario is a primary one or a layer on top of a parent scenario;
        - the title of the scenario;
        - the description of the scenario;
        - the UUID used by the CRUD API to identify the scenario.
        - the client owning the scenario and its client UUID.
        - a unique 'id' field, which is the primary key in the client's data table
        The foreign key uses the relationship. If the client is deleted, the scenarios are deleted as well.
    """
    __tablename__ = f"scenario"
    __table_args__ = {'schema': 'public'}
    
    id: int = Field(default=None, primary_key=True, index=True)
    uuid: str = Field(default=None, index=True)  # UUID
    title: str = Field(default="Default scenario")
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.now, sa_column=Column(DateTime(timezone=True)))
    
    client_id: int = Field(default=None, foreign_key="public.client.id")
    client: Client = Relationship(back_populates="scenarios")
    
    # parent_uuid: Optional[str]
    # parent: Optional["Scenario"] = Relationship(back_populates="layers")
    # layers: list["Scenario"] = Relationship(back_populates="parentScenario",
    #                                         sa_relationship_kwargs={"cascade": "save-update, merge, delete"})
    
    metrics: "Metrics" = Relationship(back_populates="scenario")


# Various categorization enums
# (Not) Dynamically create the Metrics table in the new schema. The Metrics tables stores raw impact cause metrics
# for all the Scenarios of a Client.
class Metrics(SQLModel, table=True):
    """ The Metrics table stores the data of all the Scenarios of a Client.
        Each row is tagged with the scenario ID and an auto-incremented index
    """
    __tablename__ = "metrics"
    __table_args__ = {'schema': 'agronovae'}
    id: int = Field(default=None, primary_key=True)
    scenario_id: int = Field(default=None, foreign_key="public.scenario.id", index=True)
    scenario: Scenario = Relationship(back_populates="metrics")
    
    # Raw metric integrated over the emission period
    value: float
    unit: str
    
    # Emission calculation -> compute total emission
    emission_factor: Optional[float]
    
    # Time interval
    start: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    end: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    
    # time_index defines which emissions are in the "scope" of a defined time interval.
    # is end for own and upstream emissions, and start for downstream ones.
    time_index: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    # Categorization system on a single 64-bit integer
    category_flags: int = Field(default=None, sa_column=Column(BigInteger(), default=0))
    

# Packed field service functions:


# Database engine
engine = create_engine("postgresql://natixar:dfe6f125-024e-45fb-ac03-fbe66e10531c@confiance.lan:15432/impacts")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_scenario(session: Session, scenario: Scenario) -> Scenario:
    # Complete the scenario
    if scenario.uuid is None:
        scenario.uuid = str(uuid.uuid4())
    
    # Store
    session.add(scenario)
    session.commit()
    session.refresh(scenario)
    return scenario


def create_client(session: Session, client: Client) -> Client:
    """
    :param session: a session in a Session context (with block)
    :param client: a partially filled-in client object
    :return:
    """
    # Complete the client
    if client.uuid is None:
        client.uuid = str(uuid.uuid4())
    # Create the client
    try:
        session.add(client)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError("Cannot create client!")

    # Default scenario (uses relationship)
    scenario = Scenario(title="default", client_id=client.id)
    try:
        create_scenario(session, scenario)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError("Cannot create default scenario!")
    
    session.refresh(client)
    
    client.default_scenario = scenario.uuid
    session.commit()
    
    # Create the client schema in the database and adjust the search_path (for queries)
    # session.execute(text("CREATE SCHEMA IF NOT EXISTS :client_uuid"), {"client_uuid": client.uuid})
    
    # session.execute(text("SET search_path TO :client_uuid, public"), {"client_uuid": client.id})
    
    session.refresh(client)
    return client


def load_grdf_data(session: Session, client: Client, data_file: str) -> None:
    """ Load data from a GRDF file into the database.
    """
    # Get the default scenario
    try:
        statement = select(Scenario).where(Scenario.uuid == client.default_scenario)
        results = session.exec(statement)
        scenario = results.one()
    except Exception as e:
        raise ValueError("Cannot find default scenario!")
    
    # Emission factors
    gaz_naturel_base_carbone_europe = 0.205  # kgCO2e/kWh PCI
    pcs_to_pci_factor = 1.111
    formula = lambda pcs: gaz_naturel_base_carbone_europe * (pcs / pcs_to_pci_factor)
    
    # Open the CSV file
    with open(data_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            # Create a new Metrics object
            metric = Metrics(
                scenario_id=scenario.id,
                value=row[2],
                unit="kWh_PCS",
                emission_factor=formula(1),  # emission factor kgCO2e/kWh_PCS
                start=datetime.fromisoformat(row[0]),
                end=datetime.fromisoformat(row[1]),
                time_index=datetime.fromisoformat(row[1]),
            )
            session.add(metric)
    session.commit()
    
            
def main():
    # Create the database and tables
    create_db_and_tables()
    with Session(engine) as session:
        try:
            statement = select(Client).where(Client.uuid == "7b7b43d1-51de-494c-a049-cd27c7cbe62c")
            results = session.exec(statement)
            client = results.one()
        except Exception:
            client = create_client(session, Client(name="Agro Novae Industries SAS"))
        print(client)
        load_grdf_data(session, client, "données_gaz_2022-2023.csv")

if __name__ == "__main__":
    main()
