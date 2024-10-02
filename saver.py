import psycopg2
from time import sleep
from main import make_array

from info import host,user,password,db_name


counter = 0
def info_saver (array):
    global counter
    for i in array:
        with connection.cursor () as cursor:
            cursor.execute(
            f"INSERT INTO info VALUES ({counter},'{i[0]}','{i[1]}','{i[2]}') on conflict (id) do nothing"
        )
        print (f"Added VALUES ({counter},'{i[0]}','{i[1]}','{i[2]}'")
        counter += 1

try:
    connection = psycopg2.connect(host=host,user=user,password=password,database = db_name)
    connection.autocommit = True
    info_saver(make_array())

except Exception as _ex:
    print (_ex)
finally:
    if connection:
        connection.close()
        print ("Closed")