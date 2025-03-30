# fobj = open("lang.txt","r")
# print(fobj.read())

with open("lang.txt","r") as fobj:
    for line in fobj:
        print(line.strip())


#with open("C:\\Users\\Admin\\Desktop\\Pre-Test.txt","r") as fobj1:
# r is rawstring
with open(r"C:\Users\Admin\Desktop\Pre-Test.txt","r") as fobj1:
    for line in fobj1:
        print(line)


import csv
try:
    with open("lang.txt") as fobj2:
        reader = csv.reader(fobj2)
        for line in reader:
            print(line)
except(IndexError, KeyError) as err:
    print("error")
except Exception as err:
    print("exception "+err)


import pandas as pd
print (pd.read_csv("lang.txt"))

# will display all the list of builtin exceptions and functions
print(dir(__builtins__))

