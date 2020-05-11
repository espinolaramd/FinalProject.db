#Diego Espinola
#05.08.2020
#Final project/ DataBase Talbe with ERD.

import sqlite3
from sqlite3 import Error
def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn

connection = create_connection("Assignment13.db")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

create_customer_table = """
CREATE TABLE IF NOT EXISTS customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first TEXT NOT NULL,
  last TEXT NOT NULL,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip TEXT NOT NULL
);
"""
execute_query(connection,create_customer_table)

create_book_table = """
CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    ISBN TEXT NOT NULL  ,
    edition TEXT NOT NULL,
    price TEXT NOT NULL,
    publisher TEXT NOT NULL
);
    """
execute_query(connection,create_book_table)

create_order_table = """
CREATE TABLE IF NOT EXISTS Order_t (
    number INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    total TEXT NOT NULL,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);
    """
execute_query(connection,create_order_table)

create_orderlineitem_table = """
CREATE TABLE IF NOT EXISTS order_line_item (
    order_number INTEGER,  
    book_id INTEGER,
    Quantity TEXT NOT NULL, 
    PRIMARY KEY (order_number, book_id)
    FOREIGN KEY (order_number) REFERENCES Order_t (number),
    FOREIGN KEY (book_id) REFERENCES book (book_id)
);
"""
execute_query(connection,create_orderlineitem_table)

#----------------------------------------------------------------------
Menu = 0
while Menu != 5:
    print('1)Customers table \n2)Books table \n3)Orders table \n4)Order line item \n5)Exit Program')
    Menu = int(input("Welcome, please select the table:"))
    if Menu == 1:
        print("Customers menu:")
        print('1)Add a new customer')
        print('2)Modify an existing customer')
        print('3)Print a list of all customers')
        print('4)Delete a customer')
        print('5)Return to main menu')
        option = int(input("\n>"))
        if option == 1:
            print("Please enter the details for the person:")
            first_name = input("What is the first name?")
            last_name = input("What is the last name?")
            street_address = input("What is the street address?")
            city = input("What is the city?")
            state = input("What is the state?")
            zip_code = input("What is the zip code?")

            create_customer = f"""
            INSERT INTO
                 customers (first, last, address, city, state, zip)
            VALUES
                ('{first_name}', '{last_name}', '{street_address}', '{city}', '{state}', '{zip_code}');
            """
            execute_query(connection, create_customer)
        if option == 2:
            print("Please enter the details you want to edit")
            modify = input()
            print("Please enter the new information:")
            new_inforation = input()
            print("Please enter the old information:")
            old_information = input()

            update_person_name = f"""
            UPDATE
                customers
            SET
                {modify} = '{new_inforation}
            WHERE 
                {modify} = '{old_information}
            """
            execute_query(connection,update_person_name)
        if option == 3:
            select_customers = "SELECT * from customers"
            people = execute_read_query(connection,select_customers)

            for person in people:
                print(person)

        if option == 4:
                print("Please enter the details of the costumer you want to delete")
                last_name_delete = input("last name \n>")
                delete_customer = f"""
                
                DELETE FROM
                    customers
                WHERE
                    last = '{last_name_delete}'
                """
                execute_query(connection,delete_customer)
                print(f"{last_name_delete} was deleted")
    elif Menu == 2:
        print("Books Menu")
        print("Books menu:")
        print('1)Add a new book')
        print('2)Modify an existing book')
        print('3)Print a list of all books')
        print('4)Delete a book')
        print('5)Return to main menu')
        option = int(input("\n>"))
        if option == 1:
            print("Please enter the details for the book")
            book_title = input("What is tht title")
            book_author = input("What is the book author")
            book_ISBN = input("What is the ISBN")
            book_edition = input("What is the book edition")
            book_price = input("What is the book price")
            book_publisher = input("What is the book's price")

            create_book = f"""
            INSERT INTO
                book (title, author, ISBN, edition, price, publisher)
            VALUES
                ('{book_title}', '{book_author}', '{book_ISBN}', '{book_edition}', '{book_price}', '{book_publisher}');
            """
            execute_query(connection,create_book)
        if option == 2:
            print("Please enter the details you want to edit:")
            modify = input()
            print("please enter the new information:")
            new_inforation_books = input()
            print('Please enter the old information')
            old_information_books = input()

            update_book = f"""
            UPDATE 
                book
            SET
                {modify} = '{new_inforation_books}'
            WHERE
                {modify} = '{old_information_books}'
            """
            execute_query(connection,update_book)
        if option == 3:
            select_books = "SELECT * FROM book"
            books = execute_read_query(connection,select_books)
            for x in books:
                print(x)
        if option == 4:
            print("Please enter the details of the costumer you want to delete")
            book_title_delete = input('book title \n>')

            delete_book = f"""
            DELETE FROM
                book
            WHERE 
                title = '{book_title_delete}'
            """
            execute_query(connection,delete_book)
    elif Menu == 3:
        print("Welcome to the Order table: select what do you want to do:")
        print("1)Add order")
        print("2)print order")
        option = int(input("\n>"))
        if option == 1:
            print("Please enter the details for the Order:")
            date = input("What is the date?")
            total = input("What is the total`?")
            customer_id = int(input("What is the customer id you want to associate?"))



            create_order = f"""
            INSERT INTO
                 Order_t (date, total, customer_id)
            VALUES
                ('{date}', '{total}','{customer_id} );
            """

            execute_query(connection, create_order)
        elif option == 2:
            select_orders = "SELECT * FROM Order_t"
            orders_books = execute_read_query(connection, select_orders)

            for y in orders_books:
                print(y)
    elif Menu == 4:
        print("Welcome to the Order line item menu")
        print("1) Add item")
        print("2) print Order line item menu")
        option = int(input())
        if option == 1:
            print("Please enter the details of the item")
            order_number = int(input("Order number you want to associate"))
            Book_id = int(input("book id you want to associate"))
            quantity = input("The quantity you want to order of that item")

            create_item = f"""
            INSERT INTO 
                    order_line_item (order_number, book_id, Quantity)
            VALUES
                    ('{order_number}','{Book_id}','{quantity}');
            """
            execute_query(connection,create_item)
        if option == 2:
            select_item = "SELECT * FROM order_line_item"
            item = execute_read_query(connection,select_item)

            for z in item:
                print(z)














