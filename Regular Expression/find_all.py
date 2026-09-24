import re 
text ="Python 10 java 20 C++ 34"
numbers = re.findall(r"\d+",text)

print("Numbers found:",numbers)