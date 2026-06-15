from fastapi import FastAPI
from pydantic import BaseModel
from services.payroll_service import (
    load_payroll,
    process_payroll,
    get_payroll_by_id,
    get_payroll_by_check_number)

app = FastAPI()

class PayrollInput(BaseModel):
    employee_id: int
    hours_worked: float
    
@app.get("/")
def home():
    return {"message": "Payroll API Running"}

@app.get("/payroll")
def get_payroll():
    payroll = load_payroll()

    return{"count": len(payroll), "payroll": payroll}

@app.get("/payroll/id/{payroll_id}")
def get_payroll_by_id(payroll_id: int):
    payroll = load_payroll()

    for record in payroll:
        if record["payroll_id"] == payroll_id:
            return record

    return {"message": "Payroll record not found"}

@app.get("/payroll/check/{check_number}")
def find_payroll_by_check_number(check_number: str):
    payroll_record = get_payroll_by_check_number(check_number)

    if payroll_record:
        return payroll_record

    return {"message": "Payroll record not found"}

@app.post("/payroll")
def add_payroll(payroll_input: PayrollInput):
    payroll_record = process_payroll(
        payroll_input.employee_id,
        payroll_input.hours_worked)

    if payroll_record:
        return {"message": "Payroll processed successfully", "payroll": payroll_record}

    return {"message": "Employee not found"}


