file = open("ex.txt", "r+")

data = file.read()

print("Old Data:")
print(data)

file.write("\nNew data added using r+")

file.close()

print("Data written successfully")