import mysql.connector

# Function to connect to the MySQL database


def connect():
    # Establishing the connection to the database
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root123',
        database='database7'
    )
    # Creating a cursor object to interact with the database
    cur = db.cursor()
    return db, cur

# Function to disconnect from the MySQL database


def disconnect(db, cur_d):
    # Closing the cursor
    cur_d.close()
    # Closing the connection to the database
    db.close()

# Function to insert data into the database


def insert_data(name, book, price, count, type, gener, sum):
    # Connecting to the database
    db, cur_d = connect()
    # Executing the SQL INSERT command
    cur_d.execute('INSERT INTO test7(name,book,price,count,type,gener,sum) VALUES (%s,%s,%s,%s,%s,%s,%s)', [
                  name, book, price, count, type, gener, sum])
    # Committing the transaction to save the changes
    db.commit()
    # Disconnecting from the database
    disconnect(db, cur_d)

# Function to delete data from the database based on the name


def delete_data(name):
    # Connecting to the database
    db, cur_d = connect()
    # Executing the SQL DELETE command
    cur_d.execute('DELETE FROM test7 WHERE name=%s', [name])
    # Committing the transaction to save the changes
    db.commit()
    # Disconnecting from the database
    disconnect(db, cur_d)

# Function to edit/update data in the database


def edit_data(book, price, count, type, gener, sum, name):
    # Connecting to the database
    db, cur_d = connect()
    # Executing the SQL UPDATE command
    cur_d.execute('UPDATE test7 SET book=%s, price=%s, count=%s, type=%s, gener=%s, sum=%s WHERE name=%s', [
                  book, price, count, type, gener, sum, name])
    # Committing the transaction to save the changes
    db.commit()
    # Disconnecting from the database
    disconnect(db, cur_d)

# Function to search data in the database based on various fields


def search_data(name, book, price, count, type, gener, sum):
    # Connecting to the database
    db, cur_d = connect()
    # Executing the SQL SELECT command with multiple OR conditions
    cur_d.execute('SELECT * FROM test7 WHERE name=%s or book=%s or price=%s or count=%s or type=%s or gener=%s or sum=%s',
                  (name, book, price, count, type, gener, sum))
    # Fetching all the matching records
    info = cur_d.fetchall()
    # Disconnecting from the database
    disconnect(db, cur_d)
    # Returning the fetched data
    return info

# Function to fetch and display all data from the database


def show_data():
    # Connecting to the database
    db, cur_d = connect()
    # Executing the SQL SELECT command to fetch all records
    cur_d.execute('SELECT * FROM test7')
    # Fetching all the records
    info = cur_d.fetchall()
    # Disconnecting from the database
    disconnect(db, cur_d)
    # Returning the fetched data
    return info
