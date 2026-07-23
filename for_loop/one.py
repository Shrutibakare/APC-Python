# 1.print numbers to n
n = int(input("Enter n:"))
for i in range(1,n+1):
     print(i)
    
#2.print even numbers up to n
n = int(input("Enetr n:"))
for i in range(2,n+1,2):
    print(i)

#3.print odd numbers up to n
n = int(input("Enetr n:"))
for i in range(1,n+1,2):
    print(i)

#4.print 1,2,4,8,16,32..n2
n = int(input("Enter number of terms: "))
value = 1
for i in range(n):
    print(value, end=" ")
    value *= 2

#5.sum the given sequence
n = int(input("Enetr n:"))
s=0
for i in range(1,n+1):
    s+= 1/i
print("Sum:",s)    