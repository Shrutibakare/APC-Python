#6.Compute cosine series
import math

x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

sum = 1

for i in range(1, n):
    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    sum += term

print("cos(x) =", sum)


#7.Check whether sq. root of number is prime or not
import math
num = int(input("Enetr num:"))
root = int(math.sqrt(num))

if(root<2):
    print("Square root is not prime")
else:
    prime = True
    for i in range(2,root):
        if root % i==0:
            prime = False
            break
    if prime:
        print(root,"is Prime")
    else:
        print(root,"not a prime")  
              

#8.Print the pattern
for i in range(3):
    print("ABC")