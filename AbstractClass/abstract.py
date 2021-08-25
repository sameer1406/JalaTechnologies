from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

    def noofsides(self):
        print("I have 3 sides")

    def display(self):
        print("no abstract method")


ob = Polygon()
ob.noofsides()


class subclass(Polygon):
    ob1 = Polygon()
    ob1.display()


class subclass2(subclass):
    ob_subclass = subclass()
    ob_subclass.noofsides()
