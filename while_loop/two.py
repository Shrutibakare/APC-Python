#1.print sum of odd num up to n
n = int(input("Enter n:"))
i=1
sum =0
while i<=n:
    sum+=i
    i+=2
print("Sum:",sum)    

#2.print sum of even num up to n
n = int(input("Enter n:"))
i=2
sum =0
while i<=n:
    sum+=i
    i+=2
print("Sum:",sum)    

#3.Print natural num in reverse order
n=int(input("Enter n:"))
while n>=1:
    print(n)
    n = n-1

#4.Print Fibbonacci series upto n
n = int(input("Enter number of terms:-"))
a =0
b = 1
i=1
while(i<=n):
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    i+=1

#5.Print factorial of a number
n = int(input("Enter n:"))
fact =1
while n>0:
    fact = fact*n
    n = n-1
print("Factorial:",fact)    