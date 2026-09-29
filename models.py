from dataclasses import dataclass

@dataclass
class Item:
    """One inventory item."""

    id: int | None
    item_name: str
    quantity: int
    price: float