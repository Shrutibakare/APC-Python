try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    res = a/b
except ZeroDivisionError:
    print("Cannot be divided by zero")

else:
    print("Result=",res)        
    