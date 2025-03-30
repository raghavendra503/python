
mcount =0;
fcount =0;
workset = set()
workdict = dict()
import csv
try:
    with open("C:\\Users\\Admin\\Desktop\\Programs\\csvfiles\\employeeinfo.csv") as fobj:
        reader =csv.reader(fobj)
        # for line in reader:
        # #     # obj =line.split(",")[1]
        # #     # obj2 = obj.split(",")[0]
        # #     # dict(obj2
        # #     # print(obj2)
        # #     # break
        #     workclass = line[1]
        #     workset.add(workclass)
        
        # for item in workset:
        #     print(item)


        for line in reader:
            workclass =line[1]
            workdict[workclass] =1
        print(workdict)
        # for item in workdict:
        #     print(item.strip())




        # for line in reader:
        #     gender = line[9].strip()
        #     if gender == 'Male':
        #         mcount= mcount+1
        #     elif gender == 'Female':
        #         fcount = fcount+1
        
        # print("male count"+ str(mcount))
        # print("Female count"+str(fcount))



except Exception as exp:
    print(exp)