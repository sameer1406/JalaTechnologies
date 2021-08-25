# 1.Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the
# private method in main method.
# Create a sub class and try to access the private fields and methods from sub class.
class access():
    __text = "Jala Technologies"
    __place = "warangal"

    def __access(self):
        __firstname = 'sameer'
        __lastname = 'mohd'
        return __lastname + __firstname
#

#
def main():
    ob = access
    print(ob.__text)
    print(ob.__access('self'))


if __name__ == "__main__":
    main()

class subclass(access):
    def acces(self):
        print(access.__text)
        print(access.__access('self'))


obj = subclass()
obj.acces()

# 2.Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the
# same package.

class proct():
    _address = 'warangal'
    _street = 'kazipet'

    def proctt(self):
        _company = 'SGTS'
        _address = 'HYD'
        return _company + " " + _address


class proct1(proct):
    def proct1(self):
        print(proct._address)
        print(proct.proctt('self'))


proct_obj = proct1
proct_obj.proct1('self')

# 3. Create a class with PUBLIC fields and methods.
class Student:
    schoolName = 'XYZ School'

    def __init__(self, name, age):
        self.name = name
        self.age = age


std = Student("Steve", 25)
print(std.schoolName)
