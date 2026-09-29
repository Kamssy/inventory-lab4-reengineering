from database import fetch_all_items
from models import Item

LOW_STOCK_LIMIT = 20

def get_all_items() -> list[Item]:
    """Return all items from the database as Item objects."""
    return [Item(**row) for row in fetch_all_items()]

def item_value(item: Item) -> float:
    """Return the stock value of one item (quantity x price)."""
    return item.quantity * item.price

def total_stock_value(items: list[Item]) -> float:
    """Return the combined stock value of all items."""
    return sum(item_value(item) for item in items)

def highest_stock_item(items: list[Item]) -> Item | None:
    """Return the item with the highest quantity, or None if empty."""
    if not items:
        return None
    return max(items, key=lambda item: item.quantity)

def lowest_stock_item(items: list[Item]) -> Item | None:
    """Return the item with the lowest quantity, or None if empty."""
    if not items:
        return None
    return min(items, key=lambda item: item.quantity)

def is_low_stock(item: Item) -> bool:
    """Return True if an item's quantity is below the low-stock limit."""
    return item.quantity < LOW_STOCK_LIMIT