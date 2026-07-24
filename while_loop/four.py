#1.Print multiplication table
n = int(input("Enter n:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1

#2.Print largest of n
n = int(input("How many numbers: "))
i = 1
largest = None
while i <= n:
    num = int(input("Enter number: "))
    if largest is None or num > largest:
        largest = num
    i += 1
print("Largest =", largest)    

#3.Print smallest of n
n = int(input("How many numbers: "))

i = 1
smallest = None

while i <= n:
    num = int(input("Enter number: "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1

print("Smallest =", smallest)