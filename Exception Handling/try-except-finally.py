try:
    a =int(input("Enter a number:"))

    print("Number =",a)

except ValueError:
    print("Unvalid input")

finally:
    print("Program completed")
