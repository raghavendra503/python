import pymysql
# conn = pymysql.connect(host ="localhost", port=3306, user="root",password="dummy@123")
# print(conn)
# if conn:
#     cursor =conn.cursor() # cursor is used to navigate b/w records

#     query = "select * from empdb.employees"

#     cursor.execute(query)

#     for record in cursor.fetchall():
#         print(record)

#     conn.close()
# else:
#     print(" not connected")

with pymysql.connect(host ="localhost", port=3306, user="root",password="dummy@123") as conn: # with context manager connection closes automatically

    if conn:
        cursor =conn.cursor() # cursor is used to navigate b/w records
        #query = "select * from empdb.employees"
        query = "insert into empdb.employees values ('{}','{}','{}')".format("public","btech","female")

       

        cursor.execute(query)
        print(cursor.rowcount())

        for record in cursor.fetchall():
            print(record)
    else:
        print(" not connected")