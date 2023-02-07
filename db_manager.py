import mysql.connector as sql
import pandas as pd
from mysql.connector import pooling
from mysql.connector import Error


# try: 
#     # create connection pool
#     connection_pool = pooling.MySQLConnectionPool(pool_name="module2_pool",
#                                                   pool_size=5,
#                                                   pool_reset_session=True,
#                                                   host='185.212.71.102',
#                                                   database='db',
#                                                   user='u716979257_root',
#                                                   password='Superuser1234')
#     # Get connection object from a pool
#     connection_object = connection_pool.get_connection()

# except Error as e:
#     print("Error while connecting to MySQL using Connection pool ", e)
# finally:
#     # closing database connection.
#     if connection_object.is_connected():
#         cursor.close()
#         connection_object.close()
#         print("MySQL connection is closed")
        
        
def connect(db = ''):
    """ Connect to Toys MySQL database and return connection object.
    
    :param db: Optional name of the database to connect to
    :type conn: Database connection

    :param: rollback_on_error: Flag to indicate action to be taken on an exception
    :type rollback_on_error: bool
    
    :return: Connection object if successful, or None if unsuccessful
    """                  
    conn = None
    try:
        conn = sql.connect(
            host='185.212.71.102',
            user='u716979257_root',
            database = db,
            password='Superuser1234',
            connection_timeout = 1000,
            use_pure=False
            
            # host='localhost',
            # user='root',
            # database = db,
            # password='',
            # use_pure=False
            )  

        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)
    return conn

def execute_sql(query, print_bool = True, rollback_on_error=True):
    """
    Execute a single SQL statement.

    :param conn: The connection to the database
    :type conn: Database connection

    :param query: The SQL statement to be executed
    :type query: A string
    
    :param: rollback_on_error: Optional flag to indicate action to be taken on an exception
    :type rollback_on_error: bool
    
    :return: list containing a flag that indicates if the SQL operation was successful, and the Pandas data frame
    :type return: results_lst[bool, df]

    """
    results_lst = [False, None]
    conn = connect(db='u716979257_sql_module2')
    cursor = conn.cursor(buffered=True, dictionary=True)
    
    table_name_i = query.find('from ') + 5
    table_name_end_i = query.find(' ', table_name_i)
    table_str = query[table_name_i:table_name_end_i]  
    sql_action_str = query[0:query.find(' ', 0)].lower()
    
    try:
        
        cursor.execute(query)
        if sql_action_str == 'select':
            records = cursor.fetchall()
            df = records
            if len(records) > 0:
                print()
                print(f"Total number of rows in {table_str} table: {cursor.rowcount}")
                print()                
                df = pd.DataFrame(records)
                # drop index
                df.reset_index(drop=True, inplace=True)
                if print_bool: print(df)
                print()
            results_lst[1] = df
        results_lst[0] = True
            
    except Error as err:
        if rollback_on_error:
            conn.rollback()
        print(f"Error: '{err}'")
        print("SQL execution not successful")
        cursor.close()
        conn.close()
        raise
    else:
        if rollback_on_error:
            if 'AVG' not in query and 'SUM' not in query and 'COUNT' not in query:
                conn.commit() # then commit only after all statements have completed successfully
            print()
            print("SQL execution successful")
    cursor.close()
    conn.close()
    return results_lst


def execute_multiple(statements, rollback_on_error=True):
    """
    Execute multiple SQL statements.

    :param conn: The connection to the database
    :type: Database connection object

    :param statements: The statements to be executed
    :type: A list of strings

    :param: rollback_on_error: Flag to indicate action to be taken on an exception
    :type: bool

    :return: sql_success: True if successful, or False if unsuccessful
    :type return: bool
    
    """
    sql_success = False
    conn = connect(db='u716979257_sql_module2')

    try:
        cursor = conn.cursor(buffered=True)
        for statement in statements:
            cursor.execute(statement)
            if not rollback_on_error:
                conn.commit() # commit on each statement
                print(statement, "SQL statements not successful")
    except Exception as e:
        if rollback_on_error:
            conn.rollback()
        cursor.close()
        conn.close()
        raise
    else:
        if rollback_on_error:
            conn.commit() # then commit only after all statements have completed successfully
            print(statement, "Multiple SQL statements successful")
            sql_success = True
    cursor.close()
    conn.close()
    return sql_success

