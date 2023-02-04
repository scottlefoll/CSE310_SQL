import db_manager
import mysql.connector
import sqlite3
import pandas as pd
import re

from mysql.connector import Error
from db_manager import *

if __name__ == '__main__':
    
    # opening the file in read mode
    my_file = open("initialize_sql.txt", "r", encoding="utf8")
    
    # reading the file
    data = my_file.read()
    data = re.sub(r' +', ' ', data)
    
    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    sql_lst = data.replace('\n', ' ').split(";")
    my_file.close()

    conn = connect()
    execute_multiple(conn, sql_lst) # execute the SQL statements
    
    if execute_sql(conn, sql_insert):
        """Run the following SQL:          
            INSERT INTO customers (custFirstname, custLastname, custEmail, custPassword, custLevel, comments) 
            Values ('Tom', 'Stinson', 'tomstinson@gmail.com', 'Iamtired@n', 1, 'He buys a lot of Legos'),
            ('Jill', 'Hilliard', 'jilliard@aol.com', 'awert234', 3, 'Loves Hot Wheels'),
            ('Ryan', 'Phillips', 'ryanphill@outlook.com', '23434523', 3, 'Fisher Price for his kids'),
            ('Gary', 'Mitchell', 'g.mitchell@cloudnet.com', 'q2345;oiuhjag90', 3, 'Wants to special order some things.'),
            ('Mel', 'Gibson', 'melthegreat@gibson.com', 'd;opijs9', 1, 'He is hot on Nerf guns for his battles'),
            ('Fisher', 'Omara', 'romara@cbc.net', 'q2345;oiuhjag90', 3, 'Bought once - unpleasant customer.');"""
        
    
    # Run the following SQL : SELECT * from customers , to show data before the changes    
    print("Customers before changes")
    print()
    cursor = execute_sql(conn, sql_select3)
    # Run the following SQL to demonstrate updating a single record: UPDATE customers SET custLevel = 1 WHERE custEmail = 'g.mitchell@cloudnet.com';
    cursor = execute_sql(conn, sql_update1)
    # Run the following SQL: SELECT * from customers , to show the changes
    print("Customers after changes")
    print()
    cursor = execute_sql(conn, sql_select3)
    
    # Run the following SQL: SELECT * from toyStock , to show data before the changes
    print("Toy Stock before changes")
    print()
    cursor = execute_sql(conn, sql_select3)
    # Run the following SQL to demonstrate updating multiple strings in multiple records: UPDATE toyStock SET stockDesc = REPLACE(stockDesc, 'little ones', 'children') WHERE stockBrand = 'Fisher Price';
    cursor = execute_sql(conn, sql_update2)
    # Run the following SQL: SELECT * from toyStock , to show the changes
    print("Toy Stock after changes to Fisher Price toys (replacing 'little ones' with 'children') ")
    print()
    cursor = execute_sql(conn, sql_select3)
    
    # Run the following SQL to demonstrate an inner join: 
    # SELECT toyStock.stockBrand, toyStock.stockModel, toyStock.stockDesc, toyType.typeName from toyStock  
        # INNER JOIN toyType ON toyStock.typeID = toyType.typeID 
        # WHERE toyType.typeName = 'Disney'
    cursor = execute_sql(conn, sql_select1)
    
    # Run the following SQL to demonstrate retrieving records: SELECT * from toyStock
    cursor = execute_sql(conn, sql_select2)
    
    # Run the following SQL: SELECT * from toyStock , to show data before the changes
    print("Toy Stock before changes")
    print()
    cursor = execute_sql(conn, sql_select3)            
    # Run the following SQL: DELETE FROM toyStock WHERE INSTR(stockModel, 'Starship') > 0 AND stockBrand = 'Lego';      
    cursor = execute_sql(conn, sql_delete)
    # Run the following SQL: SELECT * from toyStock , to show the changes
    print("Toy Stock after deletion of all 'Lego' brand items with the word 'Starship' in the Model field")
    print()
    cursor = execute_sql(conn, sql_select3)
    
    # Run the following SQL: SELECT * from toyStock , to show data before the changes
    print("Toy Stock before changes")
    print()      
    # Run the following SQL: UPDATE toyStock SET stockImage = CONCAT('/assets', stockImage), stockThumb = CONCAT('/assets', stockThumb);
    cursor = execute_sql(conn, sql_update3)
    # Run the following SQL: SELECT * from toyStock , to show the changes
    print("Toy Stock after changes to all records to add '/assets' to the stockImage and stockThumb paths.")
    print()
    cursor = execute_sql(conn, sql_select3)

    conn.close()
  
    
     
    
     
     
     




