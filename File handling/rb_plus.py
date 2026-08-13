file = open("data.bin", "rb+")

data = file.read()

print(data)

file.write(b"New Data")

file.close()