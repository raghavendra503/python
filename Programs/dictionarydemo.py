book ={"chap1":10, "chap2":34, "chap3":45}
print(book)
print(book["chap1"])

book["chap5"] =54
print(book)

if "chap6" in book:
    print(" key exists")
else:
    print (" key not exists")

# checks value
if 10 in book.values():
    print("exists")


print(book.keys())
book.values()
book.items # output will be in key value format 

book.pop("chap1")
print(book) # to remove chap1

book.popitem # remove last item

# to combine dictioniries
newbook = {"chap77":23,"chap88":21}
finalbook = {**book, **newbook}

# ** treated as dictionary and something starts with * treated as tuple
print(finalbook)

book.update(newbook)

print(book)


for key in book.keys:
    print(key)

for key,value in book.items:
    print(key, value)




