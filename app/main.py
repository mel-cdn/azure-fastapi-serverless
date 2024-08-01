from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


@app.get("/")
def root():
    return {"message": "API health at 100%."}


@app.get("/items")
def get_items():
    return {"message": f"{len([])} Items retrieved."}


@app.get("/items/{itemId}")
def get_item(item_id: int):
    return {"message": f"[id={item_id}] Item retrieved."}


@app.post("/items")
def add_item(item: Item):
    return {"message": f"[id={item.id}] New item '{item.name}' added."}


@app.delete("/items/{itemId}")
def delete_item(item_id: int):
    return {"message": f"[id={item_id}] Item deleted."}
