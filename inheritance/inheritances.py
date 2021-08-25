class A(object):
    def getA(self):
        return ("Super Class A")

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class B(A):
    def getB(self):
        return "sub Class of A!"

    def getA(self):
        return "Super Class A, from sub class B"

    def __init__(self, age):
        self.age = age

    def getAge(self):
        return self.age


class C(B):
    def getc(self):
        return "sub class of B!!"

    def __init__(self, address):
        self.address = address

    # To get address
    def getAddress(self):
        return self.address

    def getA(self):
        return "Super Class A, from sub class C."


class aaa():
    def main(self):
        ob1 = A("Sameer")
        print(ob1.getName())
        ob2 = B("21")
        print(ob2.getAge())
        ob3 = C("warangal")
        print(ob3.getAddress())


if __name__ == "__main__":
    aaa.main('self')

ob = C('self')
print(ob.getA())
print(ob.getB())
print(ob.getc())