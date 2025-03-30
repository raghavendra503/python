print("harika")

book = ("chap1":10, "chap2":20, "chapa3":30)
#display invidual values
print(book["chap1"]) #10
print(book["chaP2"]) #20

#ADD NEW KEY VALUE PAIR
book["chap3"] = 30
book ["chap4"] = 40
book["chap5"]   = 50


book.pop("chap1")
print("after removing:",book)
