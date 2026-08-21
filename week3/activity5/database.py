import sqlite3

class Database:
  def __init__(this):
    conn = this.connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            base INT NOT NULL,
            quote INT NOT NULL,
            rate float not null,
            unique (base, quote),

            FOREIGN KEY (base) REFERENCES currencies(id) ON DELETE CASCADE,
            FOREIGN KEY (quote) REFERENCES currencies(id) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first TEXT NOT NULL,
            last TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS balances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer int NOT NULL,
            currency int NOT NULL,
            balance float NOT NULL,
            unique (customer, currency),
            FOREIGN KEY (customer) REFERENCES customers(id) ON DELETE CASCADE,
            FOREIGN KEY (currency) REFERENCES currencies(id) ON DELETE CASCADE

        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created INTEGER NOT NULL,
            base_curr INTEGER NOT NULL,
            quote_curr INTEGER NOT NULL,
            base_sum float NOT NULL,
            quote_sum float NOT NULL,
            customer int not null,
            FOREIGN KEY (customer) REFERENCES customers(id) ON DELETE CASCADE,
            FOREIGN KEY (base_curr) REFERENCES currencies(id),
            FOREIGN KEY (quote_curr) REFERENCES currencies(id)

        )
    ''')

    conn.commit()
    conn.close()

  def connect(this):
    conn = sqlite3.connect("database.db")
    return conn 

