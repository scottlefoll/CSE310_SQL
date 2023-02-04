import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='sql_module2',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
    

def execute_sql(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("SQL successful")
    except Error as err:
        print(f"Error: '{err}'")