import tkinter as tk
from tkinter import scrolledtext
import random

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Slash Mark Chatbot")

        self.chat_history = ""

        self.chat_frame = tk.Frame(master)
        self.chat_frame.pack(pady=10)

        self.chat_history_text = scrolledtext.ScrolledText(self.chat_frame, width=40, height=15, wrap=tk.WORD)
        self.chat_history_text.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        self.user_input_label = tk.Label(self.chat_frame, text="You:")
        self.user_input_label.grid(row=1, column=0, padx=5, pady=5)

        self.user_input_entry = tk.Entry(self.chat_frame, width=30)
        self.user_input_entry.grid(row=1, column=1, padx=5, pady=5)

        self.send_button = tk.Button(self.chat_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=2, padx=5, pady=5)

        self.initialize_chat()

    def initialize_chat(self):
        self.add_message_to_chat("Chatbot", "Welcome to the Chatbot! You can start chatting. Type 'bye' to exit.")

    def send_message(self):
        user_input = self.user_input_entry.get()
        self.add_message_to_chat("You", user_input)
        response = self.generate_response(user_input)
        self.add_message_to_chat("Chatbot", response)
        self.user_input_entry.delete(0, tk.END)

    def generate_response(self, user_input):
        user_input = user_input.lower()
        responses = {
            "hi": ["Hello!", "Hi there!", "Hey!"],
            "how are you?": ["I'm good, thanks for asking!", "I'm doing well, how about you?"],
            "what's your name?": ["I'm just a humble chatbot.", "I don't have a name, I'm just here to help."],
            "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
        }
        if user_input in responses:
            return random.choice(responses[user_input])
        else:
            return "I'm not sure how to respond to that."

    def add_message_to_chat(self, sender, message):
        self.chat_history += f"{sender}: {message}\n"
        self.chat_history_text.config(state=tk.NORMAL)
        self.chat_history_text.insert(tk.END, f"{sender}: {message}\n")
        self.chat_history_text.config(state=tk.DISABLED)
        self.chat_history_text.yview(tk.END)

def main():
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
