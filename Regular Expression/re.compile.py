import re 
pattern = re.compile(r"\d+")
text ="I have 25 apples and 10 oranges"
res = pattern.findall(text)
print("Numbers:",res)