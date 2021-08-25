import  re
# 1.Different ways creating a string
# we can create strings use single quote & double quote in python,
# In Python doesn't have a concept of char so everything is treated as string
a = 'sameer'
b = "sameer Mohd"

# 2. Concatenating two strings using + operator
firstName = "Jala"
LastName = "Technologies"
print(firstName + LastName)

# 3.Finding the length of the string
print(len(firstName))

# 4.Extract a string using Substring
print(LastName[0:4])

# 5.Searching in strings using index()
test_string = "Technologies"
if len(test_string) == len(LastName):
    for i in range(0, len(LastName)):
        # print(LastName[i])
        if LastName[i] is test_string[i]:
            print("true")
        else:
            print("no")
else:
    print("no")

# 6.Matching a String Against a Regular Expression With matches()
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

# 7.Comparing strings
print("Sameer" == "Sameer")
print("Sameer" < "sameer")
print("Sameer" > "sameer")
print("Sameer" != "Sameer")

# 8.startsWith(), endsWith() and compareTo()
str1 = "Jala Technologies"
# print("Q8")
# startswith()
print(str1.startswith("Jala"))
print(str1.startswith("Technologies", 4, 10))
print(str1.startswith("Jala", 8, 14))
# endswith
print(str1.endswith("Technologies"))
print(str1.endswith("Technologies", 2, 8))
print(str1.endswith("Technologies", 5, 8))

# 9.Trimming strings with strip()
str2="     Jala Technologies     "
print(str2.strip())

# 10. Replacing characters in strings with replace()
txt = "sameer baba"
x = txt.replace("baba", "mohd")
print(x)

# 11.Splitting strings with split()
word ="Jala:technologies"
print(word.split(':'))

# 12.Converting integer objects to Strings
num = 10
print(type(num))
converted_num = str(num)
print(type(converted_num))

# 13.Converting to uppercase and lowercase
lower_letter='a'
upper_letter="A"
print(lower_letter.upper())
print(upper_letter.lower())