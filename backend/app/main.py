from fastapi import FastAPI

from app.routers import health
from app.routers import identify_chemical
from app.workflow.chemSaveGraph import ChemSaveGraph


chem_graph = ChemSaveGraph()


app = FastAPI(title="ChemCheck API")

app.include_router(health.router)
app.include_router(identify_chemical.router, tags=["identify"])


@app.get("/")
def root():
    return {"message": "ChemCheck API is running"}
