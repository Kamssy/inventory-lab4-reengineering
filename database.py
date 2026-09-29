"""SQLite database access for the inventory application."""

import os
import sqlite3
from pathlib import Path

DB_PATH = Path(os.environ.get("DB_PATH", Path(__file__).parent / "inventory.db"))


def get_connection() -> sqlite3.Connection:
    """Open a connection to the SQLite database, creating its folder if needed."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the items table and seed it if empty."""
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    count = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO items (item_name, quantity, price) VALUES (?, ?, ?)",
            [
                ("Notebook", 50, 500),
                ("Pen", 200, 100),
                ("Stapler", 15, 1200),
                ("Marker", 0, 350),
            ],
        )
    conn.commit()
    conn.close()


def fetch_all_items() -> list[dict]:
    """Return every item in the database as a list of dicts."""
    conn = get_connection()
    rows = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def insert_item(item_name: str, quantity: int, price: float) -> int:
    """Insert a new item and return its new id."""
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO items (item_name, quantity, price) VALUES (?, ?, ?)",
        (item_name, quantity, price),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id