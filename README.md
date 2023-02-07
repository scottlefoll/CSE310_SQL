# Implementation of SQL Relational Database Functionality, with
# MySQL, Python and MySQL Connector

### CSE 310-04 Applied Programming - Jeremiah Pineda
### W05 Module 2 SQL Relational DB
## Scott LeFoll
## 02/04/23
## Created by Scott LeFoll

## Module 2 Overview

The software uses asuthentication credentials to establish a secure connection to the MySQL Database. This connection is then used to implement CRUD functions. The objective is to gain initial experience with a fully functional SQL relational database, and understanding of the implementation in MySQL.The ultimate goal is to integrate this functionality in to desktop and web applications in the future.

There is a basic on-screen menu that provided simple user prompts, and captures input that is used to feed the database operations. There is basic validation provided on the user input.

This application is provided for the following purpose:

To demonstrate a full range of basic database functionality in using the MySQL 
database. The functions in this module are used to authenticate the credentials, and then create, retrieve, update, and delete records in the Toy Inventory SQL relational database (CSE310 SQL Module 2). The functions in this module are used to demonstrate
authentication and the basic CRUD operations in MySQL.
    
    The following functionality is implemented:
    
    authenticate user - authenticates the user from within Python with user credentials
    retrieve records - retrieves and displays all records with dynamic selection
    create a record - creates a new record in any of the three tables
    delete a record - deletes a document from any of the three tables
    update a record - updates a document in any of the three tables

[SQL Database Programming Demo Video](https://www.youtube.com/watch?v=ebbRSO5ST6U&feature=youtu.be)

[AQL Database Programming Git Hub repo](https://github.com/scottlefoll/CSE310_SQL)


## MySQL Database Relational Database

This application is using the MySQL Relational Database. It has three tables: a stockToys table that captures a unique record for every model and brand of toy maintained in inventory, a typeToy table that maintains a list of the type of toys in inventory, and a customers table that maintains a list of all active customers.

The tables for this application have the following structures:

toyStock:
    stockID
    stockBrand
    stockModel
    stockDesc
    stockImage
    stockThumb
    stockCost
    stockQuantity
    stockHue
    typeID
    
customers:
    custID
    custFirstname
    custLastname
    custEmail
    custPassword
    custLevel
    comments

toyType
    typeID
    typeName


## Development Environment

The development environment for this application is:

Windows 10 Professional
Python 3.11.1
VS Code 1.74.3
MySQL

The dependencies for the application are:

mysql.connector
pandas
re
Error from mysql.connector


# Useful Websites

The following websites were used in the research for this application:

- [PYnative.com MySQL tutorials](https://pynative.com/python-mysql-database-connection/)
- [Stack Overflow](https://stackoverflow.com/questions/7268178/python-mysql-and-select-output-to-dictionary-with-column-names-for-keys)
- [Geeks for Geeks](https://www.geeksforgeeks.org/how-to-show-all-tables-in-mysql-using-python/)
- [W3 Schools](https://www.w3schools.com/python/python_mysql_select.asp)
- [Medium](https://medium.com/@tattwei46/how-to-use-python-with-mysql-79304bee8753)
- [Medium](https://medium.com/analytics-vidhya/connecting-python-to-mysql-8330f186c2d)
- [Medium](https://medium.com/codex/connect-to-an-mysql-database-via-python-9c88ceac999a)
- [Free Code Camp](https://www.freecodecamp.org/news/connect-python-with-sql/)

# Future Work

As I move forward with more in depth SQL database work, these are some of the features and enhancements that I want to implement:
    
    fully functional GUI frontend using tkinter
    
    implement database triggers
    
    Implement the application in Postgre and SQL Server

    Use a db.ini or YAML file to store config and connection parameters

    Implement a connection pool to share and maintain resources

    Implement the MySQL Server on both Google Cloud and AWS

