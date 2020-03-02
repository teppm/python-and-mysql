import os
import pymysql 


#connect to database 

connection = pymysql.connect(host = 'localhost',
                             user = 'teppm' ,
                             password = 'kakapea14!!2020',
                             db = 'chinook' )




try: 
    #run a query 
    with connection.cursor() as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print (result)

finally: 
    #close connection to SQL whether above was successful or not 
    connection.close()

