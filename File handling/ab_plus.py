file = open("data.bin", "ab+")

file.write(b"\nNew Data")

file.seek(0)

data = file.read()

print(data)
file.close()