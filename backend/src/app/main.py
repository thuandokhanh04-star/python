from fastapi import FastAPI

from app.api.v1.endpoints import auth, health

app = FastAPI(
    title="MiniShop API",
    version="1.0.0",
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Welcome to MiniShop API!"}