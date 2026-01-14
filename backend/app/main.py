from fastapi import FastAPI

from app.routers import health

app = FastAPI(title="ChemCheck API")

app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "ChemCheck API is running"}
