from fastapi import FastAPI
from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Salary(BaseModel):
    salary: int
    bonus: int
    taxes: int


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the salary calculation"}


@app.post("/message")
async def write_message(data: Message) -> dict:
    return {"message": data.message}


@app.get("/number/{number}")
async def multiply_number(number: int) -> dict:
    return {"message": f"{number} multplied by two is {number*2}"}


@app.post("/salary_computation")
async def compute_salary(data: Salary) -> dict:
    if data:
        total = data.salary + data.bonus - data.taxes

    return {"message": f"Your total is {total}"}
