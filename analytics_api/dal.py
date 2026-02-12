from connection import connection


def top_costumers():
    query = "" 

    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)

def customers_without_orders():
    query = "" 

    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)


def zero_credit_active_customers():
    query = "" 

    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
