import tkinter as tk
from tkinter import messagebox

class FeedbackApp:
    """
    A simple Tkinter application for collecting customer feedback.
    It collects the user's name, email, and a feedback message.
    """
    def __init__(self, master):
        # Set up the main window properties
        self.master = master
        master.title("Customer Experience Feedback")
        master.geometry("550x500") # Increased height slightly for the new header
        master.resizable(False, False) # Prevent resizing for a cleaner look

        # --- Configure Grid Layout ---
        # Allow the input column to expand slightly
        master.grid_columnconfigure(1, weight=1)

        # --- NEW: Main Title Label (Row 0) ---
        tk.Label(master, 
                 text="Please provide feedback on your experience",
                 font=("Arial", 14, "bold"),
                 fg="#333333",
                 pady=15
                 ).grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        # --- 1. Variables to hold the input data ---
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        # Feedback is handled directly via the Text widget

        # --- 2. Widgets Creation and Placement (Labels and Inputs) ---

        # Name Input (Now Row 1)
        tk.Label(master, text="Your Name:", anchor="w").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(master, textvariable=self.name_var, width=50)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Email Input (Now Row 2)
        tk.Label(master, text="Your Email:", anchor="w").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = tk.Entry(master, textvariable=self.email_var, width=50)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Feedback Input (Now Row 3)
        tk.Label(master, text="Your Feedback:", anchor="w").grid(row=3, column=0, padx=10, pady=(20, 5), sticky="nw")
        
        # The Text widget is used for feedback and is intentionally larger (height=10)
        self.feedback_text = tk.Text(master, height=10, width=40, wrap="word")
        self.feedback_text.grid(row=3, column=1, padx=10, pady=(20, 20), sticky="nsew")

        # --- 3. Submit Button (Now Row 4) ---
        self.submit_button = tk.Button(master, text="Submit Feedback", command=self.submit_feedback, 
                                       bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

    def submit_feedback(self):
        """
        Handles the submission process:
        1. Retrieves data from all fields.
        2. Prints the data to the console.
        3. Clears all input fields.
        """
        name = self.name_var.get()
        email = self.email_var.get()
        
        # Get all content from the Text widget (from line 1, character 0 to the end)
        feedback = self.feedback_text.get("1.0", tk.END).strip()

        # Input validation (simple check to ensure feedback is not empty)
        if not feedback:
            messagebox.showwarning("Incomplete Feedback", "Please enter your feedback before submitting.")
            return

        # 1. Print the collected data to the console
        print("-" * 40)
        print("FEEDBACK SUBMITTED:")
        print(f"Name: {name if name else '[Not Provided]'}")
        print(f"Email: {email if email else '[Not Provided]'}")
        print(f"Feedback:\n{feedback}")
        print("-" * 40)
        
        # 2. Clear all input fields
        
        # Clear Entry widgets (Name and Email)
        self.name_var.set("")
        self.email_var.set("")
        
        # Clear Text widget (Feedback)
        self.feedback_text.delete("1.0", tk.END)
        
        messagebox.showinfo("Thank You", "Your feedback has been submitted successfully (and printed to the console)!")


if __name__ == '__main__':
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()
