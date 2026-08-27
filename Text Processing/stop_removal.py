import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Python is a very useful programming language"
words = word_tokenize(text)
stop_words =set(stopwords.words("english"))
result =[]

for word in words:
    if word.lower() not in stop_words:
        result.append(word)

print("Original Text:")
print(text)

print("\nAfter Stopword Removal:")
print(result)        