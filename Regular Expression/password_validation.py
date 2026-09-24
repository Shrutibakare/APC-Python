import re
password = input("Enter your password")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

if re.fullmatch(pattern,password):
    print("Password is valid")

else:
    print("Password is invalid")    