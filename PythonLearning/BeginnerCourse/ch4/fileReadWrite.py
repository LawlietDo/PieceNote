# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:06:30 2017

@author: haochinnate
"""

# open(fileName [, mode][, encode])
#       mode: r(read), w(write), a(append)
#       encode: default encode is ANSI
fileContent = '''test
content
jjj
測試文字
'''

# write
f = open("testFile.txt", "w")
f.write(fileContent)
f.close()

# read
fr = open("testFile.txt", "r")
for line in fr:
    print(line, end="")    
fr.close()
print()

# "with" statement, likes using in C#
with open("testFile.txt", "r") as fr2:
    for line in fr2:
        print(line, end="")
print()
       
# read(), read the character of length 
fr3 = open("testFile.txt", "r")
string1 = fr3.read(10) # new line \n?\r? also is one character
print(string1)
fr3.close()
print()

# readlines(), each line is a element of list
with open("testFile.txt", "r") as f:
    content = f.readlines()
    print(type(content))
    print(content)
    

# open file, encoding UTF-8 without BOM
# with open("testFile.txt", "r", encoding = "UTF-8-sig") as f:

# readline([size]), 
with open("testFile.txt", "r") as f:
    print(f.readline()) # read while line
    print(f.readline(3)) # only read 3 character 
    

