from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the salary calculation"}


@app.post("/message")
async def write_message(message: str) -> dict:
    return {"message": message}
