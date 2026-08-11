# s = 'Sam'
# x = "John"
# z = """Doe"""
# print(s)
# print(x)
# print(z)


#1.Without len()
s = input("Enter a string:")
count=0
for i in s:
    count+=1
print("Count is:",count)    

#2.Count vowels,const,digits,spaces & special char
s = input("Enter a string:")
vowels = consonants = digits = spaces =special =0
for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch == " ":
        spaces+=1
    else:
        special+=1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)                       


#3.Reverse a string without ()
s = input("Enter string:")
rev =" "
for i in s:
    rev = i + rev
print("Reversed String:",rev)    


#4.Check whether str is palindrome or not
s = input("Enter string:")
rev =""
for i in s:
    rev = i + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")    

#5. Count Uppercase and Lowercase Letters
s = input("Enter a string:")
lower =0
upper = 0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("Uppercase:-",upper)            
print("Lowercase:-",lower)            

#6. Replace Characters
s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
result = ""
for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("New String =", result)

#7. Remove Spaces
s = input("Enter string:")
res = ""
for ch in s:
    if ch != " ":
        res += ch
print("String after removing spaces:",res)        

#8. Frequency of a Character
s = input("Enter a string")
ch = input("Enter char to search:")
count = 0
for i in s:
    if i == ch:
        count+=1
print("Frequency=",count)        

#9. First and Last Character
s = input("Enter a string:")
print("1st char:",s[0])
print("Last char:",s[-1])

# 10. Display ASCII Value of Each Character
s = input("Enter a string: ")
for ch in s:
    print(ch, "=", ord(ch))