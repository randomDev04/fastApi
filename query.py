from fastapi import FastAPI

api = FastAPI()

all_disc = [
    {"id": 1, "title": "Discount 1", "description": "This is the first discount.", "city": "New York", "risk": "low", "name":"John Doe"},
    {"id": 2, "title": "Discount 2", "description": "This is the second discount.", "city": "Los Angeles", "risk": "medium", "name":"Jane Smith"},
    {"id": 3, "title": "Discount 3", "description": "This is the third discount.", "city": "Chicago", "risk": "high", "name":"Bob Johnson"}
]


@api.get("/customers")
def get_customers(city:str=20, risk:str=10):
    filtered_customers = [
        c for c in all_disc
        if c["city"].lower() == city.lower() and c["risk"].lower() == risk.lower()
    ]
    return {
        "city": city,
        "risk": risk,
        "customers": filtered_customers,
        "length": len(filtered_customers)
    }