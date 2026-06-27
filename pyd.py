from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(Title="Loan Application API", description="A simple API for managing loan applications", version="1.0.0")

class LoanApplication(BaseModel):
    name:str
    age:int
    income:float
    loan_amount:float
    employment_years:int


@app.post("/predict")
def predict_loan(application: LoanApplication):
    # Simple logic for loan approval


    approved = (
        application.income >= 50000 and
        application.employment_years >= 2 and
        application.age >= 21
    )


    return {
        "applicant_name": application.name,
        "loan_amount": application.loan_amount,
        "decision": "approved"  if approved else "rejected",
        "review_income": application.income
    }