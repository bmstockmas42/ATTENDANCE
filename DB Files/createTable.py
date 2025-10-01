import sqlite3

def create_dragon_table():
    """
    Connects to the 'dragon.db' file and creates a new table
    with a name provided by the user.
    """
    try:
        # Prompt the user for the desired table name
        table_name = input("Enter the name for the new table in 'dragon.db': ")

        # Make sure the table name isn't empty
        if not table_name:
            print("Table name cannot be empty. Please try again.")
            return

        # Connect to the database file named 'dragon.db'
        conn = sqlite3.connect('dragon.db')
        cursor = conn.cursor()

        # Construct the SQL CREATE TABLE statement.
        # We'll use a f-string to insert the user's input.
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT,
            power_level INTEGER
        );
        """

        # Execute the SQL command
        cursor.execute(create_table_sql)

        # Save the changes to the database
        conn.commit()

        print(f"Table '{table_name}' created successfully in 'dragon.db'!")

    except sqlite3.Error as e:
        # Catch any errors that might occur
        print(f"An error occurred: {e}")

    finally:
        # Always close the database connection
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")

# Run the function to create the table
if __name__ == "__main__":
    create_dragon_table()