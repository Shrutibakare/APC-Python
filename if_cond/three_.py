n = int(input("Enter n:"))
if n%2==0:
    print(n,"is Even number")
else:
    print(n,"is odd number")    




year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")    

marital = input("Married? (yes/no): ")
gender = input("Gender (male/female): ")
age = int(input("Enter age: "))

if marital.lower() == "yes":
    print("Driver is Insured")

elif marital.lower() == "no":
    if gender.lower() == "male" and age > 30:
        print("Driver is Insured")
    elif gender.lower() == "female" and age > 25:
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")

else:
    print("Invalid Input")    