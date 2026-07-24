# 1. Check whether the entered number is zero or non-zero
n = int(input("Enter n:"))
if n == 0:
    print(n,"Number is zero")
else:
    print(n,"is non-zero number")    

# 2. Find the largest of two numbers
a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))
if a>b:
    print(a, "is largest number")
else:
    print(b,"is largest number")    

# 3. Check whether a number is positive or negative
n = int(input("Enter a number: "))

if n > 0:
    print("Positive Number")
elif n < 0:
    print("Negative Number")
else:
    print("Zero")

# 4. Check whether a character is a vowel or consonant
ch = input("Enter character:")
if ch in('a','e','i','o','u','A','E','I','O','U'):
    print(ch," is a Vowel")
else:
    print(ch,"is a Consonants")    