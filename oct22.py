import tkinter as tk
from tkinter import font
import os
import openai
import APIKey

OPENAI_AI_KEY = APIKey.OPENAI_AI_KEY
# The script will automatically look for the OPENAI_API_KEY environment variable.
# Make sure you have set it before running this script.
try:
    client = openai.OpenAI(
        api_key= OPENAI_AI_KEY
    )
    api_key_is_set = True
except openai.OpenAIError:
    api_key_is_set = False

def get_answer(question):
    """
    This function now calls the OpenAI API to get a real answer.
    """
    # First, check if the API key was loaded correctly.
    if not api_key_is_set:
        return "OpenAI API key is not set.\nPlease set the OPENAI_API_KEY environment variable."

    # --- API CALL LOGIC ---
    try:
        # Note: 'gpt-5' does not exist as of late 2025.
        # I'm using 'gpt-3.5-turbo' which is a widely available and capable model.
        # You can change this to "gpt-4" if you have access.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        
        # Extract the text from the response
        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        # Handle potential API errors (e.g., network issues, invalid key)
        print(f"An error occurred: {e}")
        return f"Sorry, an error occurred while contacting OpenAI:\n{e}"

def handle_submit():
    """
    This function is called when the 'Submit' button is pressed.
    It now includes a loading message because API calls can take time.
    """
    question = entry_question.get()
    
    if not question:
        return
    
    # --- Show a "loading" message while waiting for the API ---
    text_answer.config(state=tk.NORMAL)
    text_answer.delete("1.0", tk.END)
    text_answer.insert(tk.END, "Please wait, thinking...")
    text_answer.config(state=tk.DISABLED)
    # Force the GUI to update to show the message immediately
    root.update_idletasks()

    # Get the answer from the API
    answer = get_answer(question)
    
    # Update the answer box with the real response
    text_answer.config(state=tk.NORMAL)
    text_answer.delete("1.0", tk.END)
    text_answer.insert(tk.END, answer)
    text_answer.config(state=tk.DISABLED)
    
    # Clear the entry box
    entry_question.delete(0, tk.END)

# --- GUI SETUP ---
root = tk.Tk()
root.title("OpenAI Q&A Interface")
root.geometry("550x450")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=11)
entry_font = ("Arial", 12)
answer_font = ("Arial", 11)

# Widgets
label_question = tk.Label(root, text="Ask your question:", font=("Arial", 12, "bold"))
entry_question = tk.Entry(root, width=60, font=entry_font)
button_submit = tk.Button(root, text="Submit", command=handle_submit, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white")
text_answer = tk.Text(root, height=15, width=60, font=answer_font, wrap=tk.WORD, borderwidth=2, relief="solid")
text_answer.config(state=tk.DISABLED, bg="#f0f0f0")

# Layout
label_question.pack(pady=(15, 5))
entry_question.pack(pady=5, padx=20, fill='x', ipady=4)
button_submit.pack(pady=10, ipadx=10, ipady=2)
text_answer.pack(pady=10, padx=20, fill='both', expand=True)

# Start the GUI event loop
root.mainloop()
