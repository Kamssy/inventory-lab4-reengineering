"""FastAPI application exposing the inventory as a REST API."""

from fastapi import FastAPI

from controllers import (
    get_all_items,
    highest_stock_item,
    is_low_stock,
    lowest_stock_item,
    total_stock_value,
)
from database import init_db, insert_item
from models import Item, NewItem

app = FastAPI(title="Inventory API")


@app.on_event("startup")
def startup() -> None:
    """Create and seed the database when the app starts."""
    init_db()


@app.get("/items", response_model=list[Item])
def list_items():
    """Return every item in the inventory."""
    return get_all_items()


@app.get("/items/total-value")
def get_total_value():
    """Return the combined stock value of all items."""
    return {"total_stock_value": total_stock_value(get_all_items())}


@app.get("/items/highest-stock", response_model=Item)
def get_highest_stock():
    """Return the item with the highest quantity."""
    return highest_stock_item(get_all_items())


@app.get("/items/lowest-stock", response_model=Item)
def get_lowest_stock():
    """Return the item with the lowest quantity."""
    return lowest_stock_item(get_all_items())


@app.get("/items/low-stock", response_model=list[Item])
def get_low_stock_items():
    """Return items whose quantity is below the low-stock limit."""
    return [item for item in get_all_items() if is_low_stock(item)]


@app.post("/items", response_model=Item)
def create_item(new_item: NewItem):
    """Add a new item to the inventory."""
    new_id = insert_item(new_item.item_name, new_item.quantity, new_item.price)
    return Item(id=new_id, **new_item.model_dump())