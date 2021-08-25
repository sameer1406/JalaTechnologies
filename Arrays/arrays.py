# 1.Write a function to add integer values of an array
def summ():
    arr = [1, 2, 3, 4, 5]
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    print(sum)


summ()


# 2.Write a function to calculate the average value of an array of integers
def Average(lst):
    return sum(lst) / len(lst)


arr = [1, 2, 3, 4, 5]
average = Average(arr)

print("Average of the list =", average)

# 3.Write a program to find the index of an array element
element_seach = 6
arr = [1, 2, 3, 4, 5]
try:
    print(arr.index(element_seach))
except:
    print("element doesn't exist")


# 4.Write a function to test if array contains a specific value
def specific():
    element_seach = 3
    arr = [1, 2, 3, 4, 5]
    count = -1
    for i in range(0, len(arr)):
        if element_seach == arr[i]:
            count = i

    if count >= 0:
        print(count)
    else:
        print('element not found')
specific()

# 5.Write a function to remove a specific element from an array
def remove_element():
    arr = [1, 2, 3, 4, 5]
    arr.remove(4)
    print(arr)
remove_element()

# 6.Write a function to copy an array to another array
def copy_array():
    arr = [1, 2, 3, 4, 5]
    arr_copy = [None] * len(arr)
    for i in range(0, len(arr)):
        arr_copy[i] = arr[i]

    for i in range(0, len(arr_copy)):
        print(arr_copy[i], end=" ")


copy_array()
# 7.Write a function to insert an element at a specific position in the array
def insert_elemet():
    arr = [1, 2, 3, 4, 5]
    arr.insert(4, 10)
    print(arr)

insert_elemet()
# 8.Write a function to find the minimum and maximum value of an array
def min_max():
    arr = [-1, 2, 3, 4, 500]
    print("Min:",min(arr))
    print("Max:",max(arr))
min_max()

# 9.Write a function to reverse an array of integer values
def reverse_element():
    arr = [1, 2, 3, 4, 5]
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")


reverse_element()

# 10.Write a function to find the duplicate values of an array

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(Repeat(list1))

# 11. Write a program to find the common values between two arrays
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if a_set & b_set:
        print(a_set & b_set)
    else:
        print("No common elements")


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)


# 12.Write a method to remove duplicate elements from an array
class remove_duplicate():
    def remove_dups(self):
        test_list = [1, 3, 5, 6, 3, 5, 6, 1]
        print("The original list is : " + str(test_list))
        res = []
        for i in test_list:
            if i not in res:
                res.append(i)
        print("The list after removing duplicates : " + str(res))


ob = remove_duplicate
ob.remove_dups('self')


# 13. Write a method to find the second largest number in an array

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Second largest element is:", list1[-2])

# 15.Write a method to find number of even number and odd numbers in an array
class even_odd():
    def even_oddNumber(self):
        list1=[2,3,4,5,6,7,8]
        even_num=0
        odd_num=0
        for i in range(0,len(list1)):
            if list1[i]%2==0:
               even_num=even_num+1
            else:
                odd_num=odd_num+1
        print("No.of Even Numbers:",even_num)
        print("No.of Odd Numbers:",odd_num)

ob_evenOdd=even_odd()
ob_evenOdd.even_oddNumber()

# 16.Write a function to get the difference of largest and smallest value
def min_max():
    arr = [1, 2, 3, 4, 5]
    print("difference of largest and smallest value:", max(arr) - min(arr))


min_max()

# 17. Write a method to verify if the array contains two specified elements(12,23)
def two_element():
    list2 = [10, 12, 14, 23]
    list1 = [12, 23]
    count = 0
    for ele in list2:
        if ele in list1:
            count += 1
    if count == 2:
        print("yes, list 2 contains 2 elements of list 1")
    else:
        print("no, list 2 does not contain 2 elements of list 1")


two_element()

# 18.Write a program to remove the duplicate elements and return the new array
class remove_duplicate_list():
    def remove_dups_list(self):
        test_list = [1, 3, 5, 6, 3, 5, 6, 1]
        print("The original list is : " + str(test_list))
        res = []
        for i in test_list:
            if i not in res:
                res.append(i)
        print("The list after removing duplicates : " + str(res))


ob = remove_duplicate_list
ob.remove_dups_list('self')
