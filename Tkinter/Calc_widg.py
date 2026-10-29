
import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

tk.Label(root, text="Enter First Number").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Enter Second Number").pack()
e2 = tk.Entry(root)
e2.pack()

result = tk.Label(root, text="Result: ")
result.pack(pady=10)

def calculate(op):
    a = float(e1.get())
    b = float(e2.get())

    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    elif op == "/":
        if b == 0:
            result.config(text="Cannot divide by zero")
            return
        ans = a / b

    result.config(text="Result: " + str(ans))

tk.Button(root, text="Add",
          command=lambda: calculate("+")).pack()
tk.Button(root, text="Subtract",
          command=lambda: calculate("-")).pack()
tk.Button(root, text="Multiply",
          command=lambda: calculate("*")).pack()
tk.Button(root, text="Divide",
          command=lambda: calculate("/")).pack()

root.mainloop()
