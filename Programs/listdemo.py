alist = [10,43,5,32,423,52,11]

alist.append(333)
print(alist)
alist.extend([54,54,24])
print(alist)
alist.insert(2,22)
print(alist)
#alist.remove(22)  // removes value
print(alist)
alist.insert(1,"rag")
print(alist)

alist.sort()
print(alist)

alist.sort(reverse=True) #in descending order. sort will not work on alphanumberic
print(alist)
alist.reverse()
print(alist)