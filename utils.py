"""Presentation helpers: formatting only, no business logic."""

from controllers import is_low_stock
from models import Item

def format_currency(amount: float) -> str:
    """Format a number as currency with thousands separators."""
    return f"{amount:,.2f}"

def status_label(item: Item) -> str:
    """Return 'LOW STOCK' or 'OK' for an item."""
    return "LOW STOCK" if is_low_stock(item) else "OK"