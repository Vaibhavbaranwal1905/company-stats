import re
from django.db import connection

def execute_raw_query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    return tuple(cursor.fetchall())


def sort_dict_alphanumeric_keys(data_dict):
    number = int(re.sub('[^0-9]', '', data_dict[0]) )
    length = len(data_dict[0])
    return length, number
