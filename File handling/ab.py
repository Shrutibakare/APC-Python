file = open("data.bin","ab")
data = b"\nNew Binary Data"
file.write(data)
file.close()
print("Binary data appended")