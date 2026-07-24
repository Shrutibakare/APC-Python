#1.Check whetehr enter num is prime or not
n = int(input("Enter number: "))

i = 2
prime = True

if n < 2:
    prime = False

while i < n:
    if n % i == 0:
        prime = False
        break
    i += 1

if prime:
    print("Prime Number")
else:
    print("Not Prime Number")

#2.Find sum of digits
n = int(input("Enter number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10

print("Sum of digits =", sum)

#3.check num is Palindrome or not
n = int(input("Enter number: "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#4.Reverse a num
# n = int(input("Enter number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reverse =", rev)    