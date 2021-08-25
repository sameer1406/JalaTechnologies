# 1.Define a static variable and access that through a class
class Employee:
    dept = 'Information technology'

    def __init__(self, name, id):
        self.name = name  # instance variable
        self.id = id  # instance variable


print(Employee.dept)


# 2.Define a static variable and access that through a instance
class Employee:
    dept = 'Information technology'

    def hi(self):
        print("hi from method")


emp = Employee()
print(emp.dept)

# 3.Define a static variable and change within the instance
class Employee:
    dept = 'Information technology'

    def hi(self):
        print("hi from method")

emp = Employee()
emp.dept = 'Networking'
print(emp.dept)

# 4. Define a static variable and change within the class
class Employee:
    dept = 'Information technology'

    def hi(self):
        dept = 'CSE'
        print(dept)

emp = Employee()
print(Employee.hi)