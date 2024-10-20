import mysql.connector
from mysql.connector import Error

def create_database(hostname, user, password, database_name):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=hostname,
            user=user,
            password=password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create a new database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
            print(f"Database '{database_name}' created successfully!")

            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed")

hostname = 'localhost'
user = 'root'
password = 'Apple@..12'
database_name = 'alx_book_store'

create_database(hostname, user, password, database_name)
