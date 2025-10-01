import sqlite3

def update_field(table_name, field_to_edit, new_value, primary_key_value):
    """
    Connects to dragon.db and updates a field in a specific row.
    """
    try:
        conn = sqlite3.connect('dragon.db')
        cursor = conn.cursor()

        # Construct the UPDATE statement.
        # We use '?' placeholders to safely pass the values, which prevents SQL injection.
        update_sql = f"""
        UPDATE {table_name}
        SET {field_to_edit} = ?
        WHERE id = ?;
        """

        # Execute the UPDATE statement with the values provided
        cursor.execute(update_sql, (new_value, primary_key_value))
        
        # Commit the changes to the database
        conn.commit()

        print(f"Successfully updated field '{field_to_edit}' in table '{table_name}' for row with ID {primary_key_value}.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if 'conn' in locals() and conn:
            conn.close()

# Example usage:
# Assuming your table is 'dragons', you want to change the 'power_level' of the dragon with ID 1
update_field('dragons', 'power_level', 950, 1)

# Now, let's read the data again to see the change
read_table_data('dragons')