import re 
phone = input("Enter your phone number:")
pattern = r"^[0-9]{10}$"

if re.fullmatch(pattern,phone):
    print("Phone number is valid")

else:
    print("Invalid phone number")    