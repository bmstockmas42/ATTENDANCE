import sqlite3

def view_customer_data(database_name, table_name):
    """
    Connects to an SQLite database and prints all data from a specified table.
    
    Args:
        database_name (str): The name of the SQLite database file (e.g., 'customers_info.db').
        table_name (str): The name of the table to view.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        
        # Execute a query to select all data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        
        # Fetch all results
        rows = cursor.fetchall()
        
        # Get column names for headers
        column_names = [description[0] for description in cursor.description]
        print(f"--- Data from table '{table_name}' ---")
        
        # Print headers
        print(" | ".join(column_names))
        print("-" * (len(" | ".join(column_names))))
        
        # Print each row of data
        for row in rows:
            print(" | ".join(map(str, row)))
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the connection
        if conn:
            conn.close()

# --- Example Usage ---
if __name__ == "__main__":
    # Replace 'your_table_name' with the actual name of your table in customers_info.db
    # Common names might be 'customers', 'users', or 'customer_data'
    view_customer_data('customers_info.db', 'customers')