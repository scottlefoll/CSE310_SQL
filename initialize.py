import mysql.connector
import initialize_sql
import sqlite3
import pandas as pd
from mysql.connector import Error
# from python_mysql_dbconfig import read_db_config

# params = read_db_config()


def connect(db = ''):
    """ Connect to Toys MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       user='root',
                                       database = db,
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    return conn



if __name__ == '__main__':
    conn = connect()    
    mycursor = conn.cursor()
    #Droping database if it exists.
    mycursor.execute("DROP database IF EXISTS sql_module2")
    mycursor.execute("CREATE DATABASE sql_module2")
    conn.close
    
    conn = connect('sql_module2')    
    mycursor = conn.cursor()
    mycursor.execute("mycursor module2_init_sql")
    





