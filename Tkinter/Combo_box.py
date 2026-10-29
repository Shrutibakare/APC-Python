
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ComboBox Example")
root.geometry("300x200")

tk.Label(root, text="Select a Language:").pack(pady=10)

combo = ttk.Combobox(
    root,
    values=["Python", "Java", "C++", "JavaScript"]
)
combo.pack()

combo.current(0)

def show():
    result.config(text="Selected: " + combo.get())

tk.Button(root, text="Submit", command=show).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()
