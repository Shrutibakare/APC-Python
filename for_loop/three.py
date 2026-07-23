#9.produce following design
# n = int(input("Enter value:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end ="")
#     print()

n = int(input("Enter value:"))
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")   
    print()    