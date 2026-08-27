import nltk 
from nltk.tokenize import word_tokenize

text = "Python is a very easy programming language."
words = word_tokenize(text)

print("Original Sentence:")
print(text)

print("\n Words Tokens:")
print(words)
