import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Widget")
v = tk.StringVar(value="Male")
tk.Radiobutton(root,text="Male",variable=v,value="Male").pack()
tk.Radiobutton(root,text="Female",variable=v,value="Female").pack()
root.mainloop()