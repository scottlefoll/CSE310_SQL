# CSE 310-04 Applied Programming - Jeremiah Pineda
# W05 Module 2 SQL DB
# Scott LeFoll
# 02/04/23

"""This module contains functions that interact with a MySQL relational database.
    The functions in this module are used to authenticate the credentials, and then
    create, read, update, and delete records in the Toy SQL database.
    (sql_module2). The functions in this module are used to demonstrate
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
import execute_sql
import tkinter as tk

from execute_sql import *
from db_manager import *
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext


# Radiobutton callback function
def radCall():
    radSel=radVar.get()
    if   radSel == 0: monty2.configure(text='Blue')
    elif radSel == 1: monty2.configure(text='Gold')
    elif radSel == 2: monty2.configure(text='Red')
    
    
# Spinbox callback 
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')
    
    
# Button Click Event Callback Function                       
def clickMe():                                               
    action.configure(text="** I have been Clicked! **")
    aLabel.configure(foreground='red')

# Adding a Button                                            
action = ttk.Button(win, text="Click Me!", command=clickMe)  
action.grid(column=1, row=0)                                 

# Modified Button Click Function   
def clickMe():                     
    action.configure(text='Hello ' + name.get())


# Modified Button Click Callback Function
def clickMe():
    action.configure(text='Hello ' + name.get()+ ' ' + numberChosen.get())


def _quit():         # 7
    win.quit()
    win.destroy()
    exit()


# Display a Message Box
# Callback function
# def _msgBox():
#     mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2015.')   
# Display a Message Box
def _msgBox():
#    mBox.showinfo('Python Message Info Box', 'A Python GUI 
#      created using tkinter:\nThe year is 2015.')
    mBox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')
    

# Display a Message Box
def _msgBox_e():
#    mBox.showinfo('Python Message Info Box', 'A Python GUI 
#      created using tkinter:\nThe year is 2015.')
#    mBox.showwarning('Python Message Warning Box', 'A Python GUI 
#      created using tkinter:\nWarning: There might be a bug in 
#      this code.')
    mBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
    
    
# Create instance
win = tk.Tk() 
win.title("Toys Database")
win.resizable(0, 0) # Disable resizing the GUI    
# Change the main windows icon
win.iconbitmap(r'images\toy-sm.png')

# We are creating a container frame to hold all other widgets # 1
monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)                    

# Using a scrolled Text control       # 3
scrolW  = 30                          # 4
scrolH  =  3                          # 5
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)                         # 6
scr.grid(column=0, columnspan=3)      # 7

ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)

# Position Button in second row, second column (zero-based)
action.grid(column=1, row=1)

# Disable the Button Widget
action.configure(state='disabled') 
  
# Place cursor into name Entry
nameEntered.focus()         
   
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)  
number = tk.StringVar()                         
numberChosen = ttk.Combobox(monty, width=12, textvariable=number) 
numberChosen['values'] = (1, 2, 4, 42, 100)     
numberChosen.grid(column=1, row=1)              
numberChosen.current(0)                         

numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ') # 1
labelsFrame.grid(column=0, row=7)

# Place labels into the container element # 2
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=1, row=0)
ttk.Label(labelsFrame, text="Label3").grid(column=2, row=0)

# Place cursor into name Entry
nameEntered.focus()

# Place labels into the container element – vertically # 3
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)
ttk.Label(labelsFrame, text="Label1 -- sooooo much loooonger...").grid(column=0, row=0)

labelsFrame.grid(column=0, row=7, padx=20, pady=40)

for child in labelsFrame.winfo_children(): 
    child.grid_configure(padx=8, pady=4)

scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
#### scr.grid(column=0, sticky='WE', columnspan=3)
scr.grid(column=0, columnspan=3)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)

menuBar = Menu(win)                      # 1
win.config(menu=menuBar)

fileMenu = Menu(menuBar)                 # 2
fileMenu.add_command(label="New")
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New")
fileMenu.add_command(label="Exit")        # 3
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New")
fileMenu.add_separator()               # 4
fileMenu.add_command(label="Exit")

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)      # 5

helpMenu = Menu(menuBar, tearoff=0)            # 6
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

fileMenu.add_command(label="Exit", command=_quit)    # 8
    
win.mainloop()


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

    conn = connect()
    # The following statement drops the database, creates the database and inserts records.
    cursor =execute_multiple(conn, sql_lst) # execute the batch SQL statements
    cursor.close()
    conn.close()
    

    # Show the three tables after the database is created
    # Customers table
    conn = connect(db='sql_module2')
    cursor = execute_sql(conn, sql_select2, "Customers")
    cursor.close()
    # Toy Inventory table
    conn = connect(db='sql_module2')
    cursor = execute_sql(conn, sql_select3, "Toy Inventory")
    cursor.close()
    # Toy Type table
    conn = connect(db='sql_module2')
    cursor = execute_sql(conn, sql_select4, "Toy Type")
    cursor.close()
    
    
    # Run the following SQL: SELECT * from customers , to show the data before the changes
    # print("Toy Inventory table")
    # print()
    # cursor = execute_sql(conn, sql_select3)
    # df = pd.DataFrame(cursor.fetchall())
    # Markdown(df.to_markdown(index=False))
    # print()
    
    # Run the following SQL: SELECT * from customers , to show the changes
    # print("Toy Type table")
    # print()
    # cursor = execute_sql(conn, sql_select4)
    # df = pd.DataFrame(cursor.fetchall())
    # Markdown(df.to_markdown(index=False))
    # print()
    # input("Hit any key to continue")
    
    
    # Run the following SQL to demonstrate creating new records in the customer table::   
    #     INSERT INTO customers (custFirstname, custLastname, custEmail, custPassword, custLevel, comments) 
    #     Values ('Tom', 'Stinson', 'tomstinson@gmail.com', 'Iamtired@n', 1, 'He buys a lot of Legos'),
    #     ('Jill', 'Hilliard', 'jilliard@aol.com', 'awert234', 3, 'Loves Hot Wheels'),
    #     ('Ryan', 'Phillips', 'ryanphill@outlook.com', '23434523', 3, 'Fisher Price for his kids'),
    #     ('Gary', 'Mitchell', 'g.mitchell@cloudnet.com', 'q2345;oiuhjag90', 3, 'Wants to special order some things.'),
    #     ('Mel', 'Gibson', 'melthegreat@gibson.com', 'd;opijs9', 1, 'He is hot on Nerf guns for his battles'),
    #     ('Fisher', 'Omara', 'romara@cbc.net', 'q2345;oiuhjag90', 3, 'Bought once - unpleasant customer.');
    # cursor = execute_sql(conn, sql_insert1)    
    # cursor = execute_sql(conn, sql_update2)
    # cursor = execute_sql(conn, sql_select1)
    # cursor = execute_sql(conn, sql_delete)
    # cursor = execute_sql(conn, sql_update3)
    
    
    
    # Run the following SQL : SELECT * from customers , to show data before the changes    
    """
    print("Customers before changes")
    print()
    cursor = execute_sql(conn, sql_select3)
    # Run the following SQL to demonstrate updating a single record: UPDATE customers SET custLevel = 1 WHERE custEmail = 'g.mitchell@cloudnet.com';
    cursor = execute_sql(conn, sql_update1)
    # Run the following SQL: SELECT * from customers , to show the changes
    print("Customers after changes")
    print()
    df = pd.DataFrame(cursor.fetchall())
    Markdown(df.to_markdown(index=False))
    print()
    
    """
    
    # # Run the following SQL: SELECT * from toyStock , to show data before the changes
    # print("Toy Stock before changes")
    # print()
    # cursor = execute_sql(conn, sql_select3)
    # # Run the following SQL to demonstrate updating multiple strings in multiple records: UPDATE toyStock SET stockDesc = REPLACE(stockDesc, 'little ones', 'children') WHERE stockBrand = 'Fisher Price';
    # cursor = execute_sql(conn, sql_update2)
    # # Run the following SQL: SELECT * from toyStock , to show the changes
    # print("Toy Stock after changes to Fisher Price toys (replacing 'little ones' with 'children') ")
    # print()
    # cursor = execute_sql(conn, sql_select3)
    
    # # Run the following SQL to demonstrate an inner join: 
    # # SELECT toyStock.stockBrand, toyStock.stockModel, toyStock.stockDesc, toyType.typeName from toyStock  
    #     # INNER JOIN toyType ON toyStock.typeID = toyType.typeID 
    #     # WHERE toyType.typeName = 'Disney'
    # cursor = execute_sql(conn, sql_select1)
    
    # # Run the following SQL to demonstrate retrieving records: SELECT * from toyStock
    # cursor = execute_sql(conn, sql_select2)
    
    # # Run the following SQL: SELECT * from toyStock , to show data before the changes
    # print("Toy Stock before changes")
    # print()
    # cursor = execute_sql(conn, sql_select3)            
    # # Run the following SQL: DELETE FROM toyStock WHERE INSTR(stockModel, 'Starship') > 0 AND stockBrand = 'Lego';      
    # cursor = execute_sql(conn, sql_delete)
    # # Run the following SQL: SELECT * from toyStock , to show the changes
    # print("Toy Stock after deletion of all 'Lego' brand items with the word 'Starship' in the Model field")
    # print()
    # cursor = execute_sql(conn, sql_select3)
    
    # # Run the following SQL: SELECT * from toyStock , to show data before the changes
    # print("Toy Stock before changes")
    # print()      
    # # Run the following SQL: UPDATE toyStock SET stockImage = CONCAT('/assets', stockImage), stockThumb = CONCAT('/assets', stockThumb);
    # cursor = execute_sql(conn, sql_update3)
    # # Run the following SQL: SELECT * from toyStock , to show the changes
    # print("Toy Stock after changes to all records to add '/assets' to the stockImage and stockThumb paths.")
    # print()
    # cursor = execute_sql(conn, sql_select3)

    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
  
    
     
    
     
     
     




