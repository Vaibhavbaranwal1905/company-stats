from django.db import connection

def execute_raw_query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    return tuple(cursor.fetchall())
