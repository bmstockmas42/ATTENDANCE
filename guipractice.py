import tkinter as tk

class HelloTranslatorApp:
    """
    A simple Tkinter application to demonstrate changing a single label's text 
    based on button clicks.
    """

    def __init__(self, master):
        # 1. Main Window Setup
        self.master = master
        master.title("The 'Hello' Translator")
        master.geometry("480x300")
        master.resizable(False, False) # Prevent window resizing for simplicity

        # Dictionary of greetings for easy lookup
        self.greetings = {
            "english": "Hello",
            "espanol": "Hola",
            "francais": "Bonjour",
            "deutsch": "Hallo"
        }

        # --- Initial Welcome Message (Top) ---
        self.welcome_label = tk.Label(
            master, 
            text="Welcome. Select any language to see the greeting", 
            font=('Arial', 14, 'bold'),
            fg='#333333',
            pady=15
        )
        self.welcome_label.pack()

        # --- Button Frame for layout organization (Middle) ---
        # The frame will hold the buttons in a vertical stack
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        # --- Greeting Output Label (Bottom) ---
        self.greeting_label = tk.Label(
            master, 
            text="", 
            font=('Arial', 18), 
            bg='#EFEFEF', 
            fg='#0077B6',
            width=35, 
            height=2,
            relief=tk.RIDGE
        )
        self.greeting_label.pack(pady=10)

        # 2. Button Setup
        # Create buttons and link them to the update_greeting method
        self.create_button("Español", "espanol", self.button_frame)
        self.create_button("Français", "francais", self.button_frame)
        self.create_button("Deutsch", "deutsch", self.button_frame)
        self.create_button("English", "english", self.button_frame)

    def create_button(self, display_text, key, parent_frame):
        """Helper function to create a button and place it in the frame."""
        button = tk.Button(
            parent_frame, 
            text=display_text, 
            command=lambda: self.update_greeting(key), # Use lambda to pass the language key
            font=('Arial', 11), # Reduced font size
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            relief=tk.RAISED,
            padx=8, # Reduced horizontal padding
            pady=4, # Reduced vertical padding
            width=8 # Reduced button width
        )
        # Buttons stack vertically (default side=tk.TOP).
        button.pack(padx=5, pady=4) 

    def update_greeting(self, language_key):
        """
        Called when a button is clicked. 
        Updates the text of the main greeting_label based on the language key.
        """
        new_greeting = self.greetings.get(language_key, "Language not found.")
        self.greeting_label.config(text=new_greeting)


# --- Main Application Execution ---
if __name__ == "__main__":
    # Create the root window instance
    root = tk.Tk()
    
    # Initialize the application class
    app = HelloTranslatorApp(root)
    
    # Start the Tkinter event loop (mainloop is essential!)
    root.mainloop()