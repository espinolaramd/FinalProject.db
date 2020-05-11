create_order_table = """
CREATE TABLE IF NOT EXISTS order (
    number INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT NOT NULL,
    order_total TEXT NOT NULL,
    customer_id TEXT NOT NULL
);
    """
execute_query(connection,create_order_table)

create_orderlineitem_table = """
CREATE TABLE IF NOT EXISTS orderlineitem (
    order_number INTEGER PRIMARY KEY,  
    book_id INTEGER, 
    FOREIGN KEY (order_number) REFERENCES order (order_number)
    FOREIGN KEY (book_id) REFERENCES books (id)
);
"""
