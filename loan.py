from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(Title="Loan API", description="A simple API for managing loans", version="1.0.0")

class LoanRequest(BaseModel):
    amount: float
    term: int  # in months
    interest_rate: float  # annual percentage rate


@app.post("/predict", tags=["Loan"])
async def predict_loan(loan_request: LoanRequest):


    if loan_request.amount <= 0 or loan_request.term <= 0 or loan_request.interest_rate <= 0:
        decision = "Rejected"
    else:
        decision = "Approved"
    
    return {
        "amount": loan_request.amount,
        "term": loan_request.term,
        "interest_rate": loan_request.interest_rate,
        "decision": decision
    }


@app.get("/model_info/{model_name}/{version}", tags=["Model Info"])
def model_info(model_name:str, version:int):
    return {
        "model_name":model_name,
        "version":version,
        "description":"This is a simple loan approval model that predicts whether a loan will be approved or rejected based on the loan amount, term, and interest rate."
    }


@app.get("/customers", tags=["Customers"])
def get_customers(city:str, risk:str):
    return {
        "city":city,
        "risk":risk,
        "customers":[
            {"customer_id": 1, "name": "John Doe", "city": city, "risk": risk},
            {"customer_id": 2, "name": "Jane Smith", "city": city, "risk": risk}
        ]
    }