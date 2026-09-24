import re 
text = "My phone number is 878912311"
res = re.search(r"\d+",text)

if res:
    print("Found:",res.group())

else:
    print("Not found")    