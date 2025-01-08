import psycopg
import psycopg_binary
import configparser

config = configparser.ConfigParser()
config.read('database.ini')

conn_params = {
    "dbname": config['database']['dbname'],
    "user": config['database']['user'],
    "password": config['database']['password'],
    "host": config['database']['host'],
    "port": config['database']['port'],
    "application_name": config['database']['application_name']}
    

with psycopg.connect(**conn_params) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT pg_database.datname, pg_size_pretty(pg_database_size(pg_database.datname)) AS size FROM pg_database WHERE datistemplate = false;") 
        # Fetch and print the results 
        databases = cursor.fetchall()
        print("List of Databases")
        for database in databases:
            print(f"Database: {database[0]}, Size: {database[1]}")
    cursor.close()
conn.close()
