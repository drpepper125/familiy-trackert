import # Step 1: Create Database
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

# Step 3: Add Users
if db_details:
    add_user(db_details, "users", "John", "Doe")

# Step 4: Close Database
if db_details:
   close_database(db_details)
