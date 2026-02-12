from mysql_connection import connection 

def send_data(data):
    query = "" 

    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall() # type: ignore
    else:
        return f"can't create the cursor" # type: ignore 