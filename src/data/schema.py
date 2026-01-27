import sqlite3 as sq
from pathlib import Path

DB_PATH = Path("database.db")

def init_database():
    if not DB_PATH.parent.exists():
        DB_PATH.parent.mkdir()

    with sq.connect(DB_PATH) as CONNECT:
            CURSOR = CONNECT.cursor()
            CURSOR.execute(
                '''
                    CREATE TABLE IF NOT EXISTS PRODUCTS(
                        PRODUCT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT NOT NULL,
                        PRICE REAL NOT NULL CHECK (PRICE > 0),
                        QUANTITY INTEGER NOT NULL,
                        CATEGORY TEXT NOT NULL,
                        ACTIVE INTEGER NOT NULL DEFAULT 1 CHECK (ACTIVE IN (0, 1)),
                        CREATED_AT TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        UPDATED_AT TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                '''    
            )