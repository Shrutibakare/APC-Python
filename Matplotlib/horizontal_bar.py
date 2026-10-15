import matplotlib.pyplot as plt
languagess =["Java","C","Python","C++"]
students=[20,30,35,25]

plt.barh(languagess,students)
plt.title("Programming Language Preferences")
plt.xlabel("Number of Students")
plt.ylabel("Languages")

plt.show()