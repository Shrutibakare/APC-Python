import tkinter as tk

root = tk.Tk()
root.title("Entry Widget")

tk.Label(root,text="Enter name:").pack()
tk.Entry(root).pack()
root.mainloop()

