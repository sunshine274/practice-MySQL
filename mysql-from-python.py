import datetime
import pymysql

#connect to the database
connection = pymysql.connect(
    host='localhost',
    password='',
    db='Chinook'
)
try:
    #run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("delete from Friends where name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    #close the connection regardless of whether the above was successful
    connection.close()