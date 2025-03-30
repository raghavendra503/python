fobj = open("companies.txt","w"); # if file doesn't exist, it will create file
fobj.write(" added text")
print(str(1))

for val in range(1,10):
    fobj.write(str(val) + "\n");

fobj.close();


#advantage: file closes automatically when it come out of indentation
# context manager
with open("companieslist","w") as fobj:
    fobj.write("tcs\n")
    fobj.write("evernorth")
