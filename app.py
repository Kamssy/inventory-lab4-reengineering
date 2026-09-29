"""Main script: reads inventory and prints a formatted report."""

from controllers import highest_stock_item, lowest_stock_item, total_stock_value
from models import Item
from utils import format_currency, status_label

inventory: list[Item] = [
    Item(id=1, item_name="Notebook", quantity=50, price=500),
    Item(id=2, item_name="Pen", quantity=200, price=100),
    Item(id=3, item_name="Stapler", quantity=15, price=1200),
    Item(id=4, item_name="Marker", quantity=0, price=350),
]


def print_report(items: list[Item]) -> None:
    """Print the inventory as an aligned table with a low-stock warning."""
    print(f"{'Item':<12}{'Qty':>6}{'Price':>10}{'Value':>12}  Status")
    print("-" * 50)
    for item in items:
        value = format_currency(item.quantity * item.price)
        print(
            f"{item.item_name:<12}{item.quantity:>6}"
            f"{format_currency(item.price):>10}{value:>12}  {status_label(item)}"
        )


def main() -> None:
    """Run the inventory demo."""
    print("=== Inventory Report ===")
    if not inventory:
        print("No items in inventory.")
        return
    print_report(inventory)
    print()
    print(f"Total stock value: {format_currency(total_stock_value(inventory))}")
    print(f"Highest stock: {highest_stock_item(inventory).item_name}")
    print(f"Lowest stock:  {lowest_stock_item(inventory).item_name}")


if __name__ == "__main__":
    main()