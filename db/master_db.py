import json , sqlite3
#initatite database
def creat_data_base(tablename, columns=list):
    
    db_connection = sqlite3.connect(f"{tablename}.db")
    cursor = db_connection.cursor()
    cursor.execute(f"CREATE TABLE {tablename}({columns})")
    
new_db = creat_data_base("new_table_1",columns=("firstname","lastname"))