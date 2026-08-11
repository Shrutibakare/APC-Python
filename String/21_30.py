#21. Password Validator
# password = input("Enter Password: ")

# upper = lower = digit = special = 0

# for ch in password:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     elif ch.isdigit():
#         digit += 1
#     else:
#         special += 1

# if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
#     print("Valid Password")
# else:
#     print("Invalid Password")

#22. Run-Length Encoding
s = input("Enter a string:")
res=""
count = 1
for i in range(len(s)):
    if i<len(s)-1 and s[i] == s[i+1]:
        count+=1
    else:
        res+= s[i] + str(count)
        count=1
if len(res)<len(s):
    print(res)
else:
    print(s)            

#23. String Compression
s = input("Enter String: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

if len(result) < len(s):
    print(result)
else:
    print(s)

#24. Most Frequent Character
s = input("Enter String: ")

max_char = ""
max_count = 0

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Most Frequent Character =", max_char)

#25. Second Most Frequent Character
s = input("Enter String: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

first = second = 0
first_char = second_char = ""

for ch in freq:
    if freq[ch] > first:
        second = first
        second_char = first_char
        first = freq[ch]
        first_char = ch
    elif freq[ch] > second:
        second = freq[ch]
        second_char = ch

print("Second Most Frequent Character =", second_char)

#26. Caesar Cipher
text = input("Enter Message: ")
shift = int(input("Enter Shift: "))

result = ""

for ch in text:
    if ch.isalpha():
        result += chr((ord(ch) - 65 + shift) % 26 + 65) if ch.isupper() else chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch

print("Encrypted Message =", result)

#27. Email Validator
email = input("Enter Email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

#28. Word Frequency Dictionary
text = input("Enter Paragraph: ")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

#29. Sentence Reversal
sentence = input("Enter Sentence: ")

words = sentence.split()

print("Reversed Sentence =")

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

#30. String Rotation
s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, Rotation")
else:
    print("No, Not Rotation")    