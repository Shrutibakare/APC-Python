class Student:

    def __init__(self):
        print("Constructor called")
        print("Student object created")


s1 = Student()

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Shruti", 90)
s2 = Student("Rahul", 85)

s1.display()
s2.display()