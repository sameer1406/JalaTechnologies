# 1. Write a program to read text file
from mmap import mmap
import os
file1 = open("sampletext.txt", "r")
print (file1.read())
file1.close()

# 2.Write a program to write text to .txt file using InputStream
with open('MyFile.txt', 'a') as f:
    f.write(input())

# 3.Write a program to read a file stream
with open("sampletext.txt", "r") as f:
    for i in f:
        print(i)

# 4.Write a program to read a file stream supports random access
file1 = open("sampletext.txt", "r+b")
mm = mmap(file1.fileno(), 0)
print (mm[3:9])

# 5.Write a program to read a file a just to a particular index using seek()
file1.seek(20)
print(file1.tell())
print(file1.readline())
file1.close()

# 6.Write a program to check whether a file is having read access and write access permissions
print(os.access('sampletext.txt',os.R_OK))
print(os.access('sampletext.txt',os.W_OK))