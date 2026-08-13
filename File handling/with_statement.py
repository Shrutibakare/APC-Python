with open("ex.txt","w") as file:
    file.write("Welcome to Python")
print("Data written successfully")  


with open("ex.txt", "r") as file:
    data = file.read()

print(data)


with open("data.txt", "a") as file:
    file.write("\nNew data added")

print("Data appended successfully")