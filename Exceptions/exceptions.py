# 1.Write a program to generate Arithmetic Exception without exception handling
a = 10/0
print (a)


# 2.Handle the Arithmetic exception using try-catch block
try:
    a = 10 // 0
    print(a)
    # print(ArithmeticError)
except ArithmeticError:
    print("This statement is raising an arithmetic exception.")
else:
    print("Success.")

# 4. Write a program with multiple catch blocks
try:
    a=5
    b='c'
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    # print("ZeroDivisionError")
    print ('Division by zero not allowed')


# 5. Write a program to throw exception with your own message
try:
    a=5
    b='c'
    print (a/b)
except TypeError:
    print('Unsupported operation')

# 6.Write a program to create your own exception
class MyError(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return (repr(self.value))
try:
    raise (MyError(3 * 2))
except MyError as error:
    print('A New Exception occured: ', error.value)

# 7.Write a program with finally block
try:
    k = 5 // 0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('Division by zero not allowed')

# 8.Write a program to generate Arithmetic Exception
a = 10/0
print (a)

# 9.Write a program to generate FileNotFoundException
fo = open("myfile.txt","rt")
print("File opened")

# 10. Write a program to generate ClassNotFoundException
# as per my knowledge python doesn't has ClassNotFoundException
# public class Example {
#
# public static void main(String args[]) {
# try
#     {
#         Class.forName("GeeksForGeeks");
#     }
#     catch(ClassNotFoundException  ex)
#     {
#         ex.printStackTrace();
#     }
#     }
#     }


# 11. Write a program to generate IOException
# python handles the IOException as FIleNotFound or NameError or TypeError

# 12. Write a program to generate NoSuchFieldException
# python handles the NoSuchFieldException as FIleNotFound or NameError or TypeError
