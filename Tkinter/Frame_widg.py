import tkinter as tk

root = tk.Tk()
root.title("Frame Widget")

frame =tk.Frame(root,bg="lightblue")
frame.pack(padx=20,pady=20)

tk.Label(frame,text="Inside Frame").pack()
tk.Button(frame,text="Submit").pack()

root.mainloop()