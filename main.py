from fastapi import FastAPI
# from routers import user_routes, notes_routes

app = FastAPI(Title="Notes API", description="A simple API for managing notes and users", version="1.0.0")

# app.include_router(user_routes.router)
# app.include_router(notes_routes.router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}


@app.get("/customer")
async def get_customer(customer_id: int):
    return {
        "customer_id": customer_id,
        "customer": "John Doe",
        "email": "johndoe@example.com"
    }
