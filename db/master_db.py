import json, sqlite3

import sqlite3

# Initialize database
def create_database(databasename):
    try:
        db_connection = sqlite3.connect(f"{databasename}.db")
        print(f"Database '{databasename}' connected successfully.")
        return {
            "DatabaseName": databasename,
            "DatabaseConnection": db_connection
        }
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


# Create a table with specified columns
def create_table(database_connection_details, table_name, columns=()):
    try:
        if not database_connection_details:
            raise ValueError("Invalid database connection details.")
        
        cursor = database_connection_details["DatabaseConnection"].cursor()
        
        # Validate columns
        if not columns:
            raise ValueError("Columns definition cannot be empty.")
        
        columns_definition = ", ".join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})"
        
        cursor.execute(query)
        database_connection_details["DatabaseConnection"].commit()
        
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()


# Add a user to the table
def add_user(database_connection_details, table, first_name, last_name):
    try:
        if not database_connection_details:
            raise ValueError("Invalid database connection details.")
        
        cursor = database_connection_details["DatabaseConnection"].cursor()
        
        query = f"INSERT INTO {table} (first_name, last_name) VALUES (?, ?)"
        cursor.execute(query, (first_name, last_name))
        database_connection_details["DatabaseConnection"].commit()
        
        print(f"User '{first_name} {last_name}' added successfully to '{table}'.")
    except sqlite3.Error as e:
        print(f"Error adding user: {e}")
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()


# Close database connection
def close_database(database_connection_details):
    try:
        if database_connection_details:
            database_connection_details["DatabaseConnection"].close()
            print(f"Database '{database_connection_details['DatabaseName']}' closed successfully.")
    except sqlite3.Error as e:
        print(f"Error closing database: {e}")

def create_entry(database_connection_details,table,entry_id,entry_type,date,time,importance):
        cursor = database_connection_details["DatabaseConnection"].cursor()
        query = f"INSERT INTO {table} (entry_id,entry_type, date, time, importance) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (entry_id,entry_type,date,time,importance))
        database_connection_details["DatabaseConnection"].commit()
    


db_details = create_database("family_calendar")

# Step 2: Create Users Table
if db_details:
    create_table(
        db_details,
        "users",
        (
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "first_name TEXT",
            "last_name TEXT"
        )
    )

if db_details:
    create_table(
        db_details,
        "events",
        (
            "entry_id INTEGER",
            "entry_type TEXT",
            "date TEXT",
            "time TEXT",
            "importance TEXT"
        )
    )

# Step 3: Add Users
if db_details:
    add_user(db_details, "users", "John", "Doe")
    
if db_details:
    create_entry(db_details,"events",1,"Doctor's Appointment","12-06-2024","10:20","routine")

# Step 4: Close Database
if db_details:
   close_database(db_details)
