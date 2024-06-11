\c postgres
CREATE USER Natixar WITH PASSWORD 'dfe6f125-024e-45fb-ac03-fbe66e10531c';
CREATE DATABASE Impacts;
ALTER DATABASE Impacts OWNER TO Natixar;

\c Impacts
SELECT datname, pg_catalog.pg_get_userbyid(datdba) AS owner FROM pg_database WHERE datname = 'Impacts';
DROP DATABASE Impacts;