import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup function from before
def setup_database():
    conn = sqlite3.connect('customer_info.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            address TEXT,
            preferred_contact TEXT
        )
    ''')
    conn.commit()
    conn.close()

class CustomerForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Information Form")
        self.geometry("400x450")
        
        # Call the database setup
        setup_database()

        # Initialize UI components
        self.create_widgets()
    
    def create_widgets(self):
        # Create a frame for padding
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")

        # Labels and Entry fields
        fields = ["Name", "Birthday (YYYY-MM-DD)", "Email", "Phone", "Address"]
        self.entries = {}
        for i, field in enumerate(fields):
            label = tk.Label(main_frame, text=f"{field}:", anchor="w")
            label.grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(main_frame, width=40)
            entry.grid(row=i, column=1, pady=5)
            self.entries[field] = entry

        # Dropdown for preferred contact method
        contact_label = tk.Label(main_frame, text="Preferred Contact Method:", anchor="w")
        contact_label.grid(row=len(fields), column=0, sticky="w", pady=5)
        
        self.contact_options = ["Email", "Phone", "Mail"]
        self.contact_var = tk.StringVar(self)
        self.contact_var.set(self.contact_options[0])  # set default value
        
        contact_menu = tk.OptionMenu(main_frame, self.contact_var, *self.contact_options)
        contact_menu.grid(row=len(fields), column=1, sticky="ew", pady=5)
        
        # Submit button
        submit_button = tk.Button(main_frame, text="Submit", command=self.submit_data)
        submit_button.grid(row=len(fields) + 1, column=0, columnspan=2, pady=20)
    
    def submit_data(self):
        """Validates and saves the form data to the database."""
        # Get data from entry fields
        name = self.entries["Name"].get()
        birthday = self.entries["Birthday (YYYY-MM-DD)"].get()
        email = self.entries["Email"].get()
        phone = self.entries["Phone"].get()
        address = self.entries["Address"].get()
        contact = self.contact_var.get()
        
        # Basic validation
        if not name or not email:
            messagebox.showerror("Validation Error", "Name and Email are required fields.")
            return

        try:
            conn = sqlite3.connect('customer_info.db')
            cursor = conn.cursor()
            
            # SQL query to insert data
            cursor.execute('''
                INSERT INTO customers (name, birthday, email, phone, address, preferred_contact)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, birthday, email, phone, address, contact))
            
            conn.commit()
            messagebox.showinfo("Success", "Customer information submitted successfully!")
            
            # Clear the form after successful submission
            self.clear_form()

        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Email already exists. Please use a unique email.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        finally:
            conn.close()

    def clear_form(self):
        """Clears all entry fields and resets the dropdown."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.contact_var.set(self.contact_options[0])

if __name__ == "__main__":
    app = CustomerForm()
    app.mainloop()