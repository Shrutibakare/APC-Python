import matplotlib.pyplot as plt 

subjects =["C","Python","C++","Java"]
marks =[30,35,24,25]
plt.pie(marks, labels=subjects, autopct='%1.1f%%')

plt.title("Subject Distribution")
plt.show()