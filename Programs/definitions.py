# fixed arguments
def display(a,b):
    c= a+b
   # print(c)
    return c

total = display(10,20)
print(total)


# default arguments
def display(a=0,b=0,c=1):
    print(a,b,c)

display(2)
display()
display(23,4)
display(43,33,44)


# keyword arguments
def display(c,a,b):
    print(b,a,c)

display(a=10,b=20,c=30)


#variable length

def display(*args):
    for val in args:
        print(val)
display(10,2,2,4,5,3,646,564,36,3,63)

def display(**kwargs):
    for key,value in kwargs.items:
        print(key, value)

# lambda is a single liner function
display = lambda a,b : a*b
total = display(10,20)
print(total)

# use map if no of elments input equal to no. of elements output
alist = [10,20,30]
print(list(map(lambda x:x+5,alist)))
#15,25,35

alist = ["java","python","perl"]
print(list(map(lambda x:x+" programming", alist)))