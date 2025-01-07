import configparser
import psycopg

# Read credentials from a configuration file
config = configparser.ConfigParser()
config.read('database.ini')

conn_params = {
    "dbname": config['database']['dbname'],
    "user": config['database']['user'],
    "password": config['database']['password'],
    "host": config['database']['host'],
    "port": config['database']['port'],
    "application_name": config['database']['application_name'],
    
}

with psycopg.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        # Function to create a table
        def create_table(cur, table_name):
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, name VARCHAR(100),age INTEGER);"
            cur.execute(create_table_query)

        def create_many_records(table_name, number_of_records):
            assert number_of_records > 0, "Number of records must be greater than 0"
            assert cur is not None, "Cursor is not initialized"
            batch_size = 1000  # Number of records per transaction
            for i in range(1, number_of_records + 1):
                cur.execute(f"INSERT INTO {table_name} (name, age) VALUES ('Person {i}', {i})")
                if i % batch_size == 0:
                    conn.commit()  # Commit the transaction after each batch
                conn.commit()  # Commit any remaining records

        # Example usage:
        create_table(cur, "users")
        create_many_records("users", 1000000)
        # Execute the query to get table sizes 
        cur.execute("SELECT pg_database.datname, pg_size_pretty(pg_database_size(pg_database.datname)) AS size FROM pg_database WHERE datistemplate = false;") 
        # Fetch and print the results 
        databases = cur.fetchall()
        print("List of Databases")
        for database in databases:
                print(f"Database: {database[0]}, Size: {database[1]}")
    
    for db in databases: 
        dbname = db[0] 
        print(f"Database: {dbname}") # Connect to each database 
        db_conn_params = conn_params.copy() 
        db_conn_params["dbname"] = dbname 
        with psycopg.connect(**db_conn_params) as db_conn:
            with db_conn.cursor() as db_cur:
                # Query for all tables in the current database 
                db_cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';") 
                tables = db_cur.fetchall() 
                for table in tables: 
                    print(f" Table: {table[0]}")

# No need to explicitly commit or close connections, context managers handle it