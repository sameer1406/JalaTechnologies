# 1.Write a program to print your name.
print("Sameer Mohd")

# 2.Write a program for a Single line comment and multi-line comments
# this is a single line comment
# for multi- line comment one way using hash sybmol in multi-line
# for multi-line comment
"""
this is also consider as multi-line comment
"""

# 3.Define variables for different Data Types
a = 10
flag = True
c = 'a'
f = 4.55
# double is not a part python built in function
# char is also not  part python built in function
# print(type(f))-- we can use the type function to check data type of a variable

print("int: ", a)
print("bool: ", flag)
print("char/string:", c)
print("Float:", f)

# 4.Define the local and Global variables with the same name and print both variables and
# understand the scope of the variables
x = 5


def LG():
    x = 10
    print("local x:", x)


LG()
print("global x:", x)
