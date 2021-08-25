# # 1.Write a program to print “Bright IT Career” ten times using for loop
for i in range(0, 10):
    print(":Bright IT Career")

# 2.Write a java program to print 1 to 20 numbers using the while loop.
i = 1
while (i <= 20):
    print(i)
    i = i + 1

# 3.Program to equal operator and not equal operators
a, b = 10, 20
print(a == b)
print(a != b)

# 4.Write a program to print the odd and even numbers.
a = 5
if a % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 5.Write a program to print largest number among three numbers.
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

# 6.Write a program to print even number between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i = i + 1

# 7.Write a program to print 1 to 10 using the do-while loop statement.
# Python doesn't have do-while loop. But we can create a program like this.
i = 1
max = 10
while True:
    print(i)
    i = i + 1
    if i > 10:
        break

# 8.Write a program to find Armstrong number or not
n = 407
temp = n
rev = 0
while n > 0:
    rem = n % 10
    rev = rem * rem * rem + rev
    n = n // 10
    # print(rev)
if temp == rev:
    print(temp, 'Is a Armstrong number')
else:
    print(temp, 'Is Not a Armstrong number')

# 9.Write a program to find the prime or not.
num = 5
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# 10.Write a program to palindrome or not.
n = 151
if str(n) == str(n)[::-1]:
    print("Is a palindrome")
else:
    print("not a palindrome")
#
# 11. Program to check whether a number is EVEN or ODD using switch
# in python we dont have switch condition

# import java.util.Scanner;
# public class Main {
#
#     public static void main(String[] args) {
#
#         Scanner reader = new Scanner(System.in);
#
#         System.out.print("Enter a number: ");
#         int num = reader.nextInt();
#         int check=num%2;
#         switch (check) {
#             case 0:
#              System.out.println("Even Number");
#              break;
#              case 1:
#              System.out.println("Odd Number");
#              break;
#              default:
#              System.out.println("Only Numeric Values are allowed");
#         }
#     }
# }

# Print gender (Male/Female) program according to given M/F using switch

# import java.util.Scanner;#
# public class Main {
#
#     public static void main(String[] args) {
#         char check='F';
#         switch (check) {
#             case 'F':
#              System.out.println("Female");
#              break;
#              case 'M':
#              System.out.println("Male");
#              break;
#              default:
#              System.out.println("please enter M or F ");
#         }
#     }
# }
