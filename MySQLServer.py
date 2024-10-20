import mysql.connector
from mysql.connector import Error

def create_database(hostname, user, password, database_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Apple@..12"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print(f"Database '{database_name}' created successfully!")

            cursor.close()

    except mysql.connector.Error:
        print(f"Error")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed")

hostname = 'localhost'
user = 'root'
password = 'Apple@..12'
database_name = 'alx_book_store'

create_database(hostname, user, password, database_name)
