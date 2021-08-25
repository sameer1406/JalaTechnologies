# 1.Write a function for arithmetic operators(+,-,*,/)
def arithmetic():
    a, b = 10, 2
    # print(a,b)
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("division:", a / b)
    print("double division:", a // b)  # it is used to round of the numbers


arithmetic()

# 2.Write a method for increment and decrement operators(++, --)
# def inc_dec(a,b):
"""
    Increment and Decrement operators ( both pre and post) are not allowed in it.
    But In C,C++,Java,C#,PHP are as follows
    """
# print(++a) pre-increment
# print(a++) post-increment
# print(--b) pre-decrement
# print(b--) post-decrement

# inc_dec(5,10)

# 3.Write a program to find the two numbers equal or not.
# a,b=10,10
if 10 == 1:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

# 4.Program for relational operators (<,<==, >, >==)
a, b = 10, 20
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 5.Print the smaller and larger number
a, b = 100, 200
if a>b:
    print("a is larger number","b is smaller ")
else:
    print("a is smaller", "b is larger")

