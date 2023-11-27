import socket
import threading
import tkinter as tk

def send_message(event=None):
    message = entry.get()
    if message:
        client.send(message.encode('utf-8'))
        entry.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            root.after(1, update_chat, message)
        except:
            break

def update_chat(message):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, message + '\n')
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

root = tk.Tk()
root.title('Chat App')

chat_box = tk.Text(root, height=20, width=50, state=tk.DISABLED)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.bind('<Return>', send_message)
entry.pack(pady=10)

send_button = tk.Button(root, text='Send', command=send_message)
send_button.pack()

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()