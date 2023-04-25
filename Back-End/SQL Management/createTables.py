# For this just connect to the server and create the tables
# Link for the guide: https://datatofish.com/import-csv-sql-server-python/
import pyodbc

#At this point we need to connect to the database but we will do that after we make the account on azure
connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=SERVERNAME;'
                            'Database=DATABASENAME;'
                            'Trusted_Connection=yes')

table = connection.cursor()

# Now lets initialize the users table
table.execute('''
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        user_name VARCHAR(32) NOT NULL,
        user_password VARCHAR(32)
    )
''')

# Initialize the flight table
table.execute('''
    CREATE TABLE flight(
        flight_no INTEGER PRIMARY KEY,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES user_id(user_id)
    )
''')

# Initialize the points table
table.execute('''
    CREATE TABLE point(
        flight_no INTEGER,
        x_coord float,
        y_coord float,
        sig_val float,
        FOREIGN KEY (flight_no) REFERENCES flight(flight_no)
    )
''')

table.close()
connection.close()