from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter, Query
import schema, model, natixardb
from sqlalchemy.orm import Session
from typing import List, Annotated

route = APIRouter()

@app.get("/home",  status_code=status.HTTP_200_OK)
def root():
    return 'Welcome to Klio API'

# Add new record
@route.post("/", status_code= status.HTTP_201_CREATED, response_model= schema.Agronovae)
def add_item(request: schema.Agronovae):
    new_item = model.Agronovae( date_bL=request.date_bL,
                                date_creation=request.date_creation,
                                num_livraison = request.num_livraison,
                                num_ligne_bon_livraison = request.num_ligne_bon_livraison,
                                code_article=request.code_article,
                                des1=request.des1,
                                des2=request.des2,
                                quantite=request.quantite,
                                unite=request.unite,
                                lot=request.lot,
                                pays_cde=request.pays_cde,
                                cp_cde=request.cp_cde,
                                ville_cde=request.ville_cde)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Get all items: GET /
@route.get("/", status_code=status.HTTP_200_OK , response_model = List[schema.Agronovae])
async def get_all(response: Response, limit : Annotated[
        int,
        Query(
            alias="Result_limit",
            title="Result limit",
            description="Limit of the returned items",
        ),
    ] = 10 ):
    
    results = db.query(model.Agronovae).limit(limit)
    
    if  not results:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= f'No result is found')

    return results

# Get a item
@route.get("/", status_code=status.HTTP_200_OK, response_model=schema.Agronovae )
def get_item(response: Response, db: Session = Depends(natixardb.get_db), id : Annotated[
        int,
        Query(
            alias="Id agronovae",
            title="Id agronovae",
            description="Technical Id agronovae, example : 1",
        ),
    ] = None ):
    item = db.query(model.Agronovae).filter(model.Agronovae.id == id).first()

    if not item:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= f'item with the {id} is not found')

    return item

# Delete item
@route.delete("/agronovae/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(response: Response, db: Session = Depends(natixardb.get_db), id : Annotated[
        int,
        Query(
            alias="Id agronovae",
            title="Id agronovae",
            description="Technical Id agronovae, example : 1",
        ),
    ] = None ):
    item = db.query(model.Agronovae).filter(model.Agronovae.id == id)

    if not item.first():
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= f'item with the id : {id} is not found')
    
    item.delete()
    db.commit()

    return "Successful delete"from fastapi import FastAPI, status
from mangum import Mangum
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    root_path="/dev",
    title="FastAPI app for Natixar front-end and back-office services",
    description="This API manages clients and scenarios.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://*.natixar.pro", "https://*.natixar.com"],
    allow_credentials=True,  # Handled by AWS APIGateway, but need to see the JWT for application roles
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)

# Create table from models
# model.Base.metadata.create_all(engine)

app.include_router(route, prefix="/api/v0", tags = ["Agronovae"])

# Use Mangum to deploy fastapi on aws lambda
handler = Mangum(app)
