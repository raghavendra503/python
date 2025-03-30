import os
import glob
import time
import datetime
import calendar
try:

    dirName = "dir";
    for i in range(1,10):
        if not os.path.exists(dirName+str(i)):
             os.makedirs(dirName+str(i))
    
    print(os.getcwd())
    print(os.getlogin())

    print(datetime.datetime.now())
    print(datetime.datetime.today())
    print(time.strftime("%d%b%y"))
    print(calendar.calendar(2025))

    # # delete all the files in current dir
    # files = glob.glob("C:\\Users\\Admin\\Desktop\\Programs\\csvfiles\\*.csv")
    # for file in files:
    #     os.remove(file)
    

except Exception as err:
    print("error"+err)




