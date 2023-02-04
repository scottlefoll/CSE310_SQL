import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser


def connect(db = ''):
    """ Connect to Toys MySQL database and return connection object.
    
    :param db: Optional name of the database to connect to
    :type conn: Database connection

    :param: rollback_on_error: Flag to indicate action to be taken on an exception
    :type rollback_on_error: bool
    
    :return: Connection object if successful, or None if unsuccessful
    """
    
    db_params_dict = read_db_ini()
                                       
    conn = None
    try:
        conn = mysql.connector.connect(
            host=db_params_dict['host'],
            user=db_params_dict['user'],
            database=db_params_dict['database'],
            password=db_params_dict['password']
        )
        
            # host='localhost',
            # user='root',
            # database = db,
            # password=''
            
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, query, rollback_on_error=True):
    """
    Execute a single SQL statement.

    :param conn: The connection to the database
    :type conn: Database connection

    :param statement: The statement to be executed
    :type statement: A string

    :param: rollback_on_error: Optional flag to indicate action to be taken on an exception
    :type rollback_on_error: bool
    
    :return: Cursor object if successful, or None if unsuccessful
    :type return: Cursor object

    """
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("SQL successful")
    except Error as err:
        if rollback_on_error:
            conn.rollback()
        print(f"Error: '{err}'")
        raise
    else:
        if rollback_on_error:
            conn.commit() # then commit only after all statements have completed successfully
    
    return cursor
    
        

def execute_multiple(conn, statements, rollback_on_error=True):
    """
    Execute multiple SQL statements.

    :param conn: The connection to the database
    :type conn: Database connection

    :param statements: The statements to be executed
    :type statements: A list of strings

    :param: rollback_on_error: Flag to indicate action to be taken on an exception
    :type rollback_on_error: bool

    :return: Cursor object if successful, or None if unsuccessful
    :type return: Cursor object
    
    """

    try:
        cursor = conn.cursor()
        for statement in statements:
            cursor.execute(statement)
            if not rollback_on_error:
                conn.commit() # commit on each statement
                print(statement " - SQL successful")
    except Exception as e:
        if rollback_on_error:
            conn.rollback()
        raise
    else:
        if rollback_on_error:
            conn.commit() # then commit only after all statements have completed successfully
            print(statement " - SQL not successful")
    
    return cursor


def read_db_ini(filename='db.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    config = ConfigParser()
    config.read(filename)

    # get section, default to mysql
    db_ini_dict = {}
    
    params = config.items(section)
    for param in params:
        db_ini_dict[param[0]] = param[1]
    return db_ini_dict