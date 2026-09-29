from pydantic import BaseModel
class Item(BaseModel):
    """One inventory item, also used as the API response schema."""
    id: int
    item_name: str
    quantity: int
    price: float
class NewItem(BaseModel):
    """Fields required to create a new item (no id yet)."""
    item_name: str
    quantity: int
    price: float