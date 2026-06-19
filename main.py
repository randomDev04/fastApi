from fastapi import FastAPI
from routers import user_routes, notes_routes

app = FastAPI(Title="Notes API", description="A simple API for managing notes and users", version="1.0.0")

app.include_router(user_routes.router)
app.include_router(notes_routes.router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}