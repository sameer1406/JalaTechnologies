from multipledispatch import dispatch


# 1. Write two methods with the same name but different number of parameters of same type and call the methods
@dispatch(int, int)
def product(first, second):
    resultt = first + second
    print(resultt);


@dispatch(int, int, int)
def product(first, second, third):
    result1 = first * second * third
    print(result1);


@dispatch(float, float, float)
def diffparams(first, second, third):
    result = first * second * third
    print(result);


@dispatch(str, str)
def diffparams(first, second):
    # result = first * second
    print(first, second);


@dispatch(int, int)
def sameNameSameType(a, b):
    sameName = a * b
    print(sameName)


@dispatch(int, int)
def sameNameSameType(a, b):
    sameName1 = a / b
    print(sameName1)


product(2, 3, 2)
product(2, 3)
diffparams(2.2, 3.4, 2.3)
diffparams('hi', "sameer")
sameNameSameType(2, 6)
sameNameSameType(2, 7)
