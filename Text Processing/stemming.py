import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

text = "playing played plays studies studying happily"

words = word_tokenize(text)

stemmer = PorterStemmer()

print("Original words:")
print(words)

print("\nAfter Stemming:")

for word in words:
    print(word, "->", stemmer.stem(word))