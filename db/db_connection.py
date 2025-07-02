import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Database")
            return connection

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None
