name = "Raghavendra is now in lab"
print(name)

#slicing
print(name[0]) # R
print(name[0:17:2]) # 0 to 17 characters , every 2nd charavcers
print(name[0:8])
print (name[::])
print(name[::5])
print(name[::-1])

print(name.upper())
print(name.capitalize())
print(name.title())
print(name.count("p"))
print(name.startswith("R"))

if name.startswith("R") :
    print("string is upper")
    print(" indentation")
elif name.endswith("b") :
    print(" i am in else if")
else :
    print("inside else")

print(" out of block")

print (name.split(" "))
print(name.find("is no")) # if found returns starting index, if not found returns -1
if 'is' in name:
    print("substring exists")
else :
    print("substring not exists")

print(name.replace("Raghavendra","Gupta"))

aname =" python  "
print(len(aname))
print(aname.strip()) # remove whitespaces at bothe end
print(aname.rstrip()) # remove whitespaces at right end

for val in name:
    print(val)

for val in range(1,10):
   print(val)

for val in name[::-1]: # to print string in reverse
    print(val)

