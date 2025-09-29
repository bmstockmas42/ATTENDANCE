import tkinter as tk

# --- Function to be called by the button ---
def button_action():
    """Gets text from the entry box and updates the output label."""
    input_text = text_entry.get()
    output_label.config(text=f"you entered: {input_text}!")

# --- Main Window Setup ---
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x300")

# --- Widgets ---
# Text Entry Box
text_entry = tk.Entry(root, width=15)
text_entry.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="Enter your name above and click the button.")
output_label.pack(pady=10)

# Button
my_button = tk.Button(root, text="Click me", command=button_action)
my_button.pack(pady=5)

# --- Start the Application ---
root.mainloop()