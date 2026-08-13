file = open("data.bin","wb")
data = b"Hello Python"
file.write(data)
file.close()
print("Binary data written")