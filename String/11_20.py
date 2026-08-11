#11. Word Count
sentence = input("Enter sentence:")
word = sentence.split()
print("Word count=",len(word))

#12. Longest Word
sentence = input("Enter sentence:")
word = sentence.split()
longest = word[0]
for i in word:
    if len(i)>len(longest):
        longest = i
print("Longest word:",longest)   

#13. Shortest Word
sentence = input("Enter sentence:")
word = sentence.split()
shortest = word[0]
for i in word:
    if len(i) < len(shortest):
        shortest = i
print("Shortest word:",shortest)    

#14. Title Case (First letter of every word in uppercase)
sentence = input("Enter sentence:")
print("Title Case=",sentence.title())

#15. Duplicate Characters
s = input("Enter a string: ")
print("Duplicate characters are:")
for i in s:
    if s.count(i) > 1:
        print(i)


#16. Character Frequency
s = input("Enter a string: ")
for i in set(s):
    print(i,"=",s.count(i))

#17. Anagram Check
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#18. Remove Duplicate Characters
s = input("Enter string:")
res=""
for ch in s:
    if ch not in res:
        res += ch

print("New String =", res)

#19. Substring Search
main = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in main:
    print("Substring Found")
else:
    print("Substring Not Found")

#20. Count Occurrences of a Word
sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")
words = sentence.split()
count = 0
for w in words:
    if w == word:
        count += 1
print("Occurrences =", count)   