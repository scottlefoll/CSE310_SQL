# CSE 310-04 Applied Programming - Jeremiah Pineda
# W05 Module 2 SQL DB
# Scott LeFoll
# 02/04/23

"""This module contains functions that interact with a MySQL relational database.
    The functions in this module are used to authenticate the credentials, and then
    create, read, update, and delete records in the Toy SQL database.
    (u716979257_sql_module2). The functions in this module are used to demonstrate
    authentication and the basic CRUD operations in a SQL relational database.
    
    The following functionality is implemented:
    
    authenticate user - simple authentication with username and password
    
    create a record - creates a new record in the Toy Inventory
    retrieve all records - retrieves and displays all documents in the Toy Inventory
    retrieve a single record - searches and displays a specific record in the Toy Inventory
    update a record - updates a record in the Toy Inventory
    delete a record - deletes a record from the Toy Inventory
        
"""

import db_manager
import re
import sql

from sql import *
from db_manager import *


def create_record_query(table_str):
    """
    Gets user input to and builds the query string to create a record.

    :param table_str: A valid table name from the Toys Inventory Database
    :type: a string
    
    :return: sql query string
    :type return: a string

    """
    new_record_dict = {}
    
    match table_str:
        case 'customers':
            print("Enter the following information for the new customer:")
            for col in cust_cols:
                if "name" in col: 
                    input_str = input(f"{col}: ").title().replace(" ", "")
                elif "email" in col:
                    while True:
                        input_str = input(f"{col}: ").lower()
                        if '@' not in input_str:
                            print("Invalid email address. Please try again.")
                            print()
                            continue
                        else:
                            break
                elif "Level" in col:
                    while True:
                        input_str = input(f"{col}: ").lower()
                        if input_str not in ['1', '2', '3']:
                            print("Invalid customer level. Must be 1, 2, or 3. Please try again.")
                            print()
                            continue
                        else:
                            break
                else:                    
                    input_str = input(f"{col}: ")
                new_record_dict[col] = input_str
            query_str = f'''INSERT INTO {table_str} ({', '.join(new_record_dict.keys())}) VALUES ({', '.join([f'"{val}"' for val in new_record_dict.values()])})'''
            
        case 'toyStock':
            print("Enter the following information for the new toy:")
            for col in toy_cols:
                if "typeId" in col:
                    lookup_sql_str = retrieve_records_query('toyType', True)
                    results_lst = execute_sql(conn, lookup_sql_str)
                    lookup_df = results_lst[1]
                    print()
                    while True:
                        input_str = input(f"Enter typeID for the new Toy Record from the Toy Type table above: ")
                        try:
                            input_int = int(input_str)
                        except:
                            print("Invalid entry. Must be an integer. Please try again.")
                            print()
                            continue
                        if input_int not in lookup_df['typeId'].values:
                            print("Invalid entry. Please try again.")
                            print()
                            continue
                        else:
                            break
                elif "Brand" in col or "Model" in col: 
                    input_str = input(f"{col}: ").title()
                elif "Cost" in col or "Quantity" in col:
                    while True:
                        input_str = input(f"{col}: ").lower()
                        if not re.match(r'^[0-9]+(\.[0-9]{1,2})?$', input_str):
                            print("Invalid entry. Must be a number with up to 2 decimal places. Please try again.")
                            print()
                            continue
                        else:
                            break
                else:
                    input_str = input(f"{col}: ")
                new_record_dict[col] = input_str
            query_str = f'''INSERT INTO {table_str} ({', '.join(new_record_dict.keys())}) VALUES ({', '.join([f'"{val}"' for val in new_record_dict.values()])})'''
            
        case 'toyType':
            print("Enter the following information for the new toy type:")
            for col in type_cols:
                input_str = input(f"{col}: ").title()
                new_record_dict[col] = input_str
            query_str = f'''INSERT INTO {table_str} ({', '.join(new_record_dict.keys())}) VALUES ({', '.join([f'"{val}"' for val in new_record_dict.values()])})'''
            
    return query_str


def retrieve_records_query(table_str, all=False):
    """
    Gets user input and builds the query string to retrieve (a) record(s).

    :param table_str: A valid table name from the Toys Inventory Database
    :type: a string
    
    :return: sql query string
    :type return: a string

    """
    match table_str:
        case 'customers':
            if all: return f"SELECT * FROM {table_str}"
            input_str = input("Enter the customer ID, the last name, or the email of the Customer to retrieve (hit enter to retrieve all records): ").lower().replace(" ", "")
            if input_str == '': return f"SELECT * FROM {table_str}"
            try:
                input_int = int(input_str)
                query_str = f"SELECT * FROM {table_str} WHERE custId = {input_int}"
            except:
                if '@' in input_str:
                    query_str = f"SELECT * FROM {table_str} WHERE custEmail = '{input_str}'"
                else:
                    input_str = input_str.title()
                    input_str2 = input(f"Enter the first name for the '{input_str}' customer to retrieve, or hit 'enter' to search last name only: ")
                    if input_str2 == '': 
                        query_str = f"SELECT * FROM {table_str} WHERE custLastName = '{input_str}'"
                    else:
                        query_str = f"SELECT * FROM {table_str} WHERE custLastName = '{input_str}' AND custFirstname = '{input_str2}'"
        case 'toyStock':
            if all: return f"SELECT * FROM {table_str}"
            input_str = input("Enter the Id or the brand for the Toy to retrieve (hit enter to retrieve all records): ")
            if input_str == '': return f"SELECT * FROM {table_str}"
            try:
                input_int = int(input_str)
                query_str = f"SELECT * FROM {table_str} WHERE stockId = {input_int}"
            except:
                input_str2 = input(f"Enter the model for the {input_str} brand to retrieve, or hit 'enter' to retrieve the entire {input_str} brand: ")
                query_str = f"SELECT * FROM {table_str} WHERE stockModel = '{input_str}' AND stockBrand = '{input_str2}'"
        case 'toyType':
            if all: return f"SELECT * FROM {table_str}"
            input_str = input("Enter the typeId or the toy type name to retrieve (hit enter to retrieve all records): ")
            if input_str == '': return f"SELECT * FROM {table_str}"
            try:
                input_int = int(input_str)
                query_str = f"SELECT * FROM {table_str} WHERE typeId = {input_int}"
            except:
                query_str = f"SELECT * FROM {table_str} WHERE typeName = '{input_str}'"
    
    return query_str


def update_record_query(table_str):
    """
    Gets user input and builds the query string to update a record.

    :param table_str: A valid table name from the Toys Inventory Database
    :type: a string
    
    :return: sql query string
    :type return: a string

    """
    update_record_dict = {}
    
    match table_str:
        case 'customers':
            lookup_sql_str = retrieve_records_query(table_str, True)
            results_lst = execute_sql(conn, lookup_sql_str)
            lookup_df = results_lst[1]
            cust_cols = list(lookup_df)
            print()
            while True:
                print()        
                input_str = input("Enter the Customer ID of the Customer to update from the table above: ")
                try:
                    input_int = int(input_str)
                    lookup_df = lookup_df[lookup_df['custID'] == int(input_str)]
                    lookup_df = lookup_df.reset_index(drop=True)
                except:
                    print("Invalid entry. Must be an integer. Please try again.")
                    print()
                    continue
                if input_int not in lookup_df['custID'].values:
                    print("Invalid entry. Please try again.")
                    print()
                    continue
                else:
                    # drop the custID column from the lookup_df
                    update_record_dict = lookup_df.to_dict('records')[0]
                    break

            print()        
            print("Enter the following information to update the customer record:")
            print()
            print("These are the current values for the record you selected:")
            print()
            print(lookup_df)
            print()
            print("Note: If you do not want to update a field, just hit 'enter' to leave it unchanged.")
            print()
            for col in cust_cols:
                if "ID" in col: 
                    update_record_dict[col] = int(update_record_dict[col])
                    continue
                if 'name' in col:
                    input_str = input(f"{col}: {update_record_dict[col]} \tupdated value: ").title()
                else:
                    input_str = input(f"{col}: {update_record_dict[col]} \tupdated value: ")
                if input_str != '':
                    update_record_dict[col] = input_str
                    u = update_record_dict                  
            query_str = f'''UPDATE {table_str} SET custFirstname = "{u['custFirstname']}", custLastname = "{u['custLastname']}", 
                            custEmail = "{u['custEmail']}", custPassword = "{u['custPassword']}", custLevel = "{u['custLevel']}", 
                            comments = "{u['comments']}" WHERE custID = {u['custID']}'''
            
        case 'toyStock':
            lookup_sql_str = retrieve_records_query(table_str, True)
            results_lst = execute_sql(conn, lookup_sql_str)
            lookup_df = results_lst[1]
            cust_cols = list(lookup_df)
            print()
            while True:
                print()        
                input_str = input("Enter the Toy Stock ID of the Toy to update from the table above: ")
                try:
                    input_int = int(input_str)
                    lookup_df = lookup_df[lookup_df['stockId'] == int(input_str)]
                    lookup_df = lookup_df.reset_index(drop=True)
                except:
                    print("Invalid entry. Must be an integer. Please try again.")
                    print()
                    continue
                if input_int not in lookup_df['stockId'].values:
                    print("Invalid entry. Please try again.")
                    print()
                    continue
                else:
                    # drop the custID column from the lookup_df
                    update_record_dict = lookup_df.to_dict('records')[0]
                    break
            
            print()        
            print("Enter the following information to update the toy record:")
            print()
            print("These are the current values for the record you selected:")
            print()
            print(lookup_df)
            print()
            print("Note: If you do not want to update a field, just hit 'enter' to leave it unchanged.")
            print()
            for col in cust_cols:
                if "stockId" in col: 
                    update_record_dict[col] = int(update_record_dict[col])
                    continue
                if 'Brand' in col or 'Model' in col:
                    input_str = input(f"{col}: {update_record_dict[col]} \tupdated value: ").title()
                else:
                    input_str = input(f"{col}: {update_record_dict[col]} \tupdated value: ")
                if input_str != '':
                    update_record_dict[col] = input_str
                    u = update_record_dict                  
            query_str = f'''UPDATE {table_str} SET stockBrand = "{u['stockBrand']}", stockModel = "{u['stockModel']}", 
                            stockDesc = "{u['stockDesc']}", stockImage = "{u['stockImage']}", stockThumb = "{u['stockThumb']}", 
                            stockCost = "{u['stockCost']}", stockQuantity = "{u['stockQuantity']}", stockHue = "{u['stockHue']}"
                            WHERE stockId = {u['stockId']}'''

        case 'toyType':        
            lookup_sql_str = retrieve_records_query(table_str, True)
            results_lst = execute_sql(conn, lookup_sql_str)
            lookup_df = results_lst[1]
            cust_cols = list(lookup_df)
            print()
            while True:
                print()        
                input_str = input("Enter the Type ID to update from the table above: ")
                try:
                    input_int = int(input_str)
                    lookup_df = lookup_df[lookup_df['typeId'] == int(input_str)]
                    lookup_df = lookup_df.reset_index(drop=True)
                except:
                    print("Invalid entry. Must be an integer. Please try again.")
                    print()
                    continue
                if input_int not in lookup_df['typeId'].values:
                    print("Invalid entry. Please try again.")
                    print()
                    continue
                else:
                    # drop the custID column from the lookup_df
                    update_record_dict = lookup_df.to_dict('records')[0]
                    break
                
            print()        
            print("Enter the following information to update the toy type record:")
            print()
            print("These are the current values for the record you selected:")
            print()
            print(lookup_df)
            print()
            print("Note: If you do not want to update a field, just hit 'enter' to leave it unchanged.")
            print()
            for col in cust_cols:
                if "typeId" in col: 
                    update_record_dict[col] = int(update_record_dict[col])
                    continue
                if 'Name' in col:
                    input_str = input(f"{col}: {update_record_dict[col]} \tupdated value: ").title()
                if input_str != '':
                    update_record_dict[col] = input_str
                    u = update_record_dict                  
            query_str = f'''UPDATE {table_str} SET typeName = "{u['typeName']}" WHERE typeId = {u['typeId']}'''

    return query_str


def delete_record_query(table_str):
    """
    Gets user input and builds the query string to delete a record.

    :param table_str: A valid table name from the Toys Inventory Database
    :type: a string
    
    :return: sql query string
    :type return: a string

    """
    match table_str:
        case 'customers':
            input_str = input("Enter the customer ID, the last name, or the email of the Customer to delete: ").lower().replace(" ", "")
            try:
                input_int = int(input_str)
                query_str = f"DELETE FROM {table_str} WHERE custId = {input_int}"
            except:
                if '@' in input_str:
                    query_str = f"DELETE FROM {table_str} WHERE custEmail = '{input_str}'"
                else:
                    input_str = input_str.title()
                    input_str2 = input(f"Enter the first name for the '{input_str}' customer to delete: ")
                    query_str = f"DELETE FROM {table_str} WHERE custLastName = '{input_str}' AND custFirstname = '{input_str2}'"
        case 'toyStock':
            input_str = input("Enter the Id or the brand for the Toy to delete: ")
            try:
                input_int = int(input_str)
                query_str = f"DELETE FROM {table_str} WHERE stockId = {input_int}"
            except:
                input_str2 = input(f"Enter the model for the {input_str} brand to delete, or hit 'enter' to delete the entire '{input_str}' brand: ")
                if input_str2 == '':
                    query_str = f"DELETE FROM {table_str} WHERE stockBrand = '{input_str}'"
                else:
                    query_str = f"DELETE FROM {table_str} WHERE stockModel = '{input_str}' AND stockBrand = '{input_str2}'"
        case 'toyType':
            input_str = input("Enter the typeId or the toy type name to delete: ")
            try:
                input_int = int(input_str)
                query_str = f"DELETE FROM {table_str} WHERE typeId = {input_int}"
            except:
                query_str = f"DELETE FROM {table_str} WHERE typeName = '{input_str}'"
                
    return query_str
    

def menu_input(action_str):
    """
    Gets user input for menu choice.

    :param action_str: An action type ("add to", "retrieve from", "update to", "delete from" )
    :type: a string
    
    :return: input_str: the name of the table to query
    :type return: a string

    """

    print()
    print("1. Customers")
    print("2. Toy Inventory")
    print("3. Toy Types")
    print()
    while True:
        
        input_str = input(f"Enter the table to {action_str} (1, 2, 3, or 'b' to go back): ").lower().replace(" ", "")
        if input_str not in ['1', '2', '3', 'b']:
            print("Please enter a valid selection")
            continue
        else:
            match input_str:
                case '1':
                    input_str = 'customers'
                case '2':
                    input_str = 'toyStock'
                case '3':
                    input_str = 'toyType'
                case 'b':
                    return input_str
            break
    return input_str


def menu_init():
    """
    Display menu and gets user input for initialization options.
    
    :returns: init_int: 0, 1, or 2
    :type return: an int

    """
    print()
    print("Please choose a database initialization option:")
    print()
    print("0. Retain Database changes - only restart the engine")
    print("1. Full Initialization - on first startup, or to reset database to original state")
    print("2. Full Initialization plus run the example CRUD SQL statements")
    print()
    while True:
        
        input_str = input(f"Startup option (0, 1, 2): ")
        if input_str not in ['0', '1', '2']:
            print("Please enter a valid option (0, 1, 2)")
            print()
            continue
        else:
            return int(input_str)


def db_initialize():
    """
    Initializes the database and inserts records.
    
    :return: : True if the database initialized successfully, exits with errors otherwise
    :type return: a bool

    """
    conn = connect()
    # The following initialization statement drops the database, creates the database and inserts records.
    sql_success = execute_multiple(conn, sql_lst) # execute the batch SQL statements
    if sql_success:
        print("The database has been created and the records have been inserted.")
        input("Hit Enter to continue...")
    else:
        print("There was an error creating the database, and no records have been inserted.")
        exit()
    conn.close()
    return True


def example_crud():
    """
    Runs a series of six (6) SQL statements to demonstrate CRUD functions from code.
    
    :return: : True if the SQL statements executed successfully, exits with errors otherwise
    :type return: a bool
    
    """
    # conn = connect(db='u716979257_sql_module2')
    conn = connect(db='sql_module2')
    
    # additional SQL statements to insert, update, and delete records as demonstrations of CRUD functions
    print("The following series of six (6) SQL executions are to demonstrate various CRUD functions from within code: ")
    print()
    # The following statement inserts 7 records into the Customers table.
    results_lst = execute_sql(conn, sql_insert1) # execute the first stored SQL statement
    if results_lst[0]:
        print()
        print("Seven (7) additional records have been created in the Customers Table through the following stored SQL query: ")
        print()
        print(sql_insert1)
        print()
        input("Hit Enter to continue...")
    else:
        print("There was an error inserting into the database.")
        exit()
        
    results_lst = execute_sql(conn, sql_update1) # execute the 2nd stored SQL statement
    if results_lst[0]:
        print()
        print("The record for the customer with email 'g.mitchell@cloudnet.com' has been updated in the customers table, using the following SQL query:")
        print()
        print(sql_update1)
        print()
        input("Hit Enter to continue...")
    else:
        print("There was an error updating the customers table.")
        exit()

    results_lst = execute_sql(conn, sql_update2) # execute the 3rd stored SQL statement
    if results_lst[0]:
        print()
        print("The toyStock inventory file has been updated using the following SQL query:")
        print()
        print(sql_update2)
        print()
        input("Hit Enter to continue...")
    else:
        print("There was an error updating the customers table.")
        exit()

    results_lst = execute_sql(conn, sql_select1) # execute the 4th stored SQL statement
    if results_lst[0]:
        print()
        print("The toyStock inventory file has been updated using the following SQL query:")
        print()
        print(sql_select1)
        print()
        input("Hit Enter to continue...")
    else:
        print("There was an error updating the customers table.")
        exit()
        
    results_lst = execute_sql(conn, sql_delete) # execute the 5th stored SQL statement
    if results_lst[0]:
        print()
        print("All Lego brand toys with Model containing the word 'Starship' have been deleted from the inventory file using the following SQL query:")
        print()
        print(sql_delete)
        print()
        input("Hit Enter to continue...")
    else:
        print("There was an error updating the customers table.")
        exit()
        
    results_lst = execute_sql(conn, sql_update3) # execute the 6th stored SQL statement
    if results_lst[0]:
        print()
        print("The stockThumb column for all toyStock inventory items has been updated to add '/assets' to the path using the following SQL query:")
        print()
        print(sql_update3)
        print()
        input("Hit Enter to continue...")
    else:
        print("There was an error updating the customers table.")
        exit()
    
    conn.close()
    return True


def menu(conn):
    """Displays a menu and asks the user for a menu choice.

    :param conn: the connection to the database
    :type: a connection object
    
    """
    while True:
        # Ask the user for a menu choice.
        print()
        print()
        print("******CSE 310 Module 2: SQL Toy Database Menu: ******")
        print()
        print("1. Create a new record")
        print("2. Retrieve records")
        print("3. Update record")
        print("4. Delete a Record")
        print("5. Exit")
        print()

        choice_str = input("Please enter a menu choice (1 - 5): ")
        if choice_str == "":
            # if the user hits 'Enter', then exit the program
            print("Exiting the program")
            exit()
        
        try:
            # try to convert the user input to int.
            choice_int = int(choice_str)
            if choice_int < 1 or choice_int > 5:
                # if the input is not in the range 0 - 9, then go back to input
                print("Please enter a valid menu choice (1 - 5)")
                continue
            else:
                # if the input is in the range 0 - 9, then execute the corresponding function
                match choice_int:
                    case 1:
                        # create a new record
                        action_str = "add to"
                        table_str = menu_input(action_str)
                        if table_str == 'b': continue
                        query_str = create_record_query(table_str)
                        execute_sql(conn, query_str)
                    case 2:
                        # retrieve records
                        action_str = "retrieve from"
                        table_str = menu_input(action_str)
                        if table_str == 'b': continue
                        query_str = retrieve_records_query(table_str)
                        execute_sql(conn, query_str)
                    case 3:
                        # update record
                        action_str = "update to"
                        table_str = menu_input(action_str)
                        if table_str == 'b': continue
                        query_str = update_record_query(table_str)
                        execute_sql(conn, query_str)
                    case 4:
                        # delete record
                        action_str = "delete from"
                        table_str = menu_input(action_str)
                        if table_str == 'b': continue
                        query_str = delete_record_query(table_str)
                        delete_str = input("Confirm Delete Record: y/n ").lower()
                        if delete_str == 'y':
                            execute_sql(conn, query_str)
                        else:
                            continue
                    case 5:
                        if conn.is_connected():
                            conn.close()
                            print("MySQL connection is closed")
                        query_str = exit()
                
        except ValueError:
            # if the int conversion throws an error, then go back to input
            print()
            print("Please enter a valid menu choice (1 - 5)")
            continue
        
print()
print()

if __name__ == '__main__':
    
    # SQL statements to create the Toy Database, with three tables
    # opening the file that contains the SQL Table Definition Query in read mode
    my_file = open("initialize_sql.txt", "r", encoding="utf8")
    # reading the file
    data = my_file.read()
    data = re.sub(r' +', ' ', data)
    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    sql_lst = data.replace('\n', ' ').split(";")
    my_file.close()

    init_int = menu_init()
    if init_int > 0:
        db_initialize()
        if init_int == 2:
            example_crud()

    # Show the three tables after the database is created
    # Customers table
    print()
    print("**************************This is the start of the Toy Inventory SQL Database Application**************************")
    print()
    print("These are the three tables at application startup:")
    print()
    conn = connect(db='sql_module2')
    results_lst = execute_sql(conn, sql_select2, "Customers")
    df = results_lst[1]
    cust_cols = list(df)
    cust_cols = cust_cols[1:]
    # Toy Inventory table
    conn = connect(db='sql_module2')
    results_lst = execute_sql(conn, sql_select3, "Toy Inventory")
    df = results_lst[1]
    toy_cols = list(df)
    toy_cols = toy_cols[1:]
    # Toy Type table
    conn = connect(db='sql_module2')
    results_lst = execute_sql(conn, sql_select4, "Toy Type")
    df = results_lst[1]
    type_cols = list(df)
    type_cols = type_cols[1:]
    
    input("hit enter to continue")
    
    menu(conn)
    
     
     
     




