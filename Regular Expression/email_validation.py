import re
email =input("Enter your email:")
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.fullmatch(pattern,email):
    print("Email is valid")

else:
    print("Email is invalid")    