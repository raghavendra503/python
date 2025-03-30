import getpass
name = input("enter a name")
password = getpass.getpass("enter password")
if len(password) == 6 and password.isupper() == True and password.find('$') ==-1 and password.find('&') ==-1 :
    print("correct")
else:
    print("incorrect") 