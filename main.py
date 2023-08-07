from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import List
app = FastAPI(title="Trading App")


class User(BaseModel):
    id: int
    role: str
    name: str


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return user_id


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float

fake_trades = []
@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status":200, "data":fake_trades}


