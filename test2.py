from google.cloud.sql.connector import Connector
import sqlalchemy

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "project:region:instance",
        "pymysql",
        user="my-user",
        password="my-password",
        db="my-db-name"
    )
    return conn


# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

# insert statement
insert_stmt = sqlalchemy.text(
    "INSERT INTO customers (custFirstname, title) VALUES (:id, :title)",
)

with pool.connect() as db_conn:
    # insert into database
    db_conn.execute(insert_stmt, id="book1", title="Book One")

    # query database
    result = db_conn.execute("SELECT * from my_table").fetchall()

    # Do something with the results
    for row in result:
        print(row)
    

connector.close()