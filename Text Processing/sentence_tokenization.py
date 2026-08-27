import nltk 
from nltk.tokenize import sent_tokenize
text = "Python is easy to learn. It is a popular programming language. I like Python."
sentences = sent_tokenize(text)

print("Original text:")
print(text)

print("\nSentences:")

for i in sentences:
    print(i)