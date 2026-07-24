# 1.Evaluate student performance
marks = int(input("Enter marks:"))
if marks>=90:
    print("Excellent Performance")
elif marks>=80:
    print("Very Good Performance")
elif marks>=70:
    print("Good Performance")   
elif marks >= 60:
    print("Average Performance")
else:
    print("Poor Performance")     

# 2. Find the largest of three numbers
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
if a>b and a>c:
    print("Largest=",a)
elif b>a and b>c:
    print("Largest=",b)
else:
    print("Largest=",c)        

#3.Samllest of three num
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest =", a)
elif b <= a and b <= c:
    print("Smallest =", b)
else:
    print("Smallest =", c)