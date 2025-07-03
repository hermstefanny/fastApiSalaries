from fastapi import FastAPI
from pydantic import BaseModel, field_validator


class Message(BaseModel):
    message: str


class Salary(BaseModel):
    salary: int
    bonus: int
    taxes: int

    @field_validator("salary", "bonus", "taxes")
    def must_be_int(cls, value, field):
        if not value:
            raise ValueError(
                f"error: 3 fields expected (salary, bonus, taxes). You forgot:{value}"
            )
        if not isinstance(value, int):
            raise ValueError("Error: expected numbers, got strings")
        return value


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

    total = data.salary + data.bonus - data.taxes

    return {"message": f"Your total is {total}"}
