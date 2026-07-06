import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# =================================
# GEMINI API KEY
# =================================

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

# =================================
# SEND MESSAGE
# =================================

def send_message():

    user_message = entry.get()

    if user_message.strip() == "":
        return

    chat_area.insert(
        tk.END,
        f"You: {user_message}\n\n"
    )

    try:

        response = model.generate_content(
            user_message
        )

        bot_reply = response.text

    except Exception as e:

        bot_reply = f"Error: {e}"

    chat_area.insert(
        tk.END,
        f"AI: {bot_reply}\n\n"
    )

    chat_area.see(tk.END)

    entry.delete(0, tk.END)

# =================================
# GUI
# =================================

root = tk.Tk()

root.title("AI Chatbot Pro")

root.geometry("800x600")

title = tk.Label(
    root,
    text="🤖 AI Chatbot Pro",
    font=("Arial", 20, "bold")
)

title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=90,
    height=25,
    font=("Arial", 11)
)

chat_area.pack(padx=10, pady=10)

entry = tk.Entry(
    root,
    width=70,
    font=("Arial", 12)
)

entry.pack(
    side=tk.LEFT,
    padx=10,
    pady=10
)

send_btn = tk.Button(
    root,
    text="Send",
    width=15,
    command=send_message
)

send_btn.pack(
    side=tk.LEFT,
    padx=5
)

root.mainloop()