atup = (30,45,23,23)
print(atup)
#atup[0]=33
#print(atup) # gives error

#but to modify tuple convert to list
data = list(atup)
data[0] =1
atup =tuple(data)
print(atup)