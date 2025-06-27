import sys
import mysql.connector
from mysql.connector import Error

DB_NAME = "alx_book_store"


def create_database():

    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Alisa_2005"  # MySQL root password  and details
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Database '{DB_NAME}' created successfully!")

    except Error as err:
        print(f"Error: '{err}'")
        sys.exit(1)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
