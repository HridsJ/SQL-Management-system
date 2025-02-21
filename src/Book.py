try : import pymysql as cntr
except ImportError : import mysql.connector as cntr
import datetime as __dt , matplotlib.pyplot as plt
from random import shuffle
from tempfile import mktemp
from os import system , startfile

__db = cntr.connect(host = 'localhost' , user = 'root' , passwd = '1234' , database = 'book_shop')
__cur = __db.cursor()
if str(cntr) == "<module 'pymysql' from 'C:\\\\Program Files (x86)\\\\Python37\\\\lib\\\\site-packages\\\\pymysql\\\\__init__.py'>" :
    __db.autocommit = True
else : __db.autocommit(True)


#Function to check is it leap year
is_leapyear = lambda year : year % 4 == 0


#Function to get last date of month
def last_month(month , year):
    if month in (1,3,5,7,8,10,12) : return 31
    elif month == 2 and is_leapyear(year) : return 29
    elif month == 2 : return 28
    else : return 30
    

clrscreen = lambda : system("cls")


def view_stock() :
    __cur.execute("select Book_No , Book_Name , Available_Stock from stock")
    data = __cur.fetchall()
    print("Book Number     Book Name            Stock")
    for row in data :
        if len(row[1]) >= 11 : print(row[0] , '           ' , row[1] , '        ' , row[2])
        else : print(row[0] , '           ' , row[1] , '               ' , row[2])

            
def add_stock() :            
    print('Add Stock'.center(89 , '='))
    bno = unique_book_no()
    if bno :
        print("Book Number : " , bno)
    else : bno = int(input("Enter book number : "))
    bname = input("Enter the Book\'s Name : ")
    auth = input("Enter the Author of the Book : ")
    publ = input("Enter the Publisher of the Book : ")
    cost = eval(input("Enter the Cost per Book : "))
    stock = int(input("Enter the Quantity purchased : "))
    __cur.execute("insert into stock values ({} , '{}' , '{}' , '{}' , {} , {} , {} , '{}')".format(bno , bname , auth , publ , cost , stock , 0, __dt.date.today()))
    print("Inserted Sucessfully !!!")
    

        
def add_user() :
    user = input("Enter the user name : ")
    passwd = input("Enter a Password : ")
    passwd2 = input("Enter Password to confirm : ")
    if passwd == passwd2 :
        __cur.execute("insert into users values('{}' , '{}')".format(user , passwd))
        print("Created Successfully!!!")
    elif passwd != passwd2 : print("You've entered different passwords")
    

        
def sell_book() :
    print('Purchase')
    cname = input("Enter the Customer Name : ")
    phno = int(input("Enter the phone number : "))
    bno = int(input("Enter book number : "))
    bname = input("Enter the name of the book : ")
    cost = eval(input("Enter the cost of the book : "))
    __cur.execute("insert into purchased values({} , '{}')".format(bno , __dt.date.today()))
    __cur.execute("update stock set qty_purchased = qty_purchased + 1 where Book_No = {}".format(bno))
    __cur.execute("update stock set Available_Stock = Available_Stock - 1 where Book_No = {}".format(bno))
    print("Bought Successfully")
    q = '''Book Shop\nName : {}\nPhone No : {}\nBook Number : {}\nBook Name : {}\nCost : {}\nDate Of Purchase : {}'''.format(cname , phno , bno , bname , cost , __dt.date.today())
    filename = mktemp('.txt')
    open(filename , 'w').write(q)
    startfile(filename , 'print')
    __cur.execute('select Book_Name , Book_No , Author from stock where Available_Stock = 0')
    if __cur.rowcount == 1 :
        print("STOCK OF ")
        print("Book Name : " , __cur.fetchall()[0][0])
        print("Book Number : " , __cur.fetchall()[0][1])
        print("Author : " , __cur.fetchall()[0][2])
        print("EXHAUSTED")
        __cur.execute('delete from stock where Available_Stock = 0')
    
        
        
def unique_book_no () :
    __cur.execute("select max(Book_No) from stock")
    data = __cur.fetchall()
    if bool(data[0][0]) :
        L1 = [x for x in range((data[0][0] + 1) , (data[0][0] + 10000))]
        shuffle(L1)
        return L1.pop(0)
    else : return False

    
def login():
    user = input("Enter the username : ")
    pwd = input("Enter the password : ")
    __cur.execute("select * from users where username = '{}' and password = '{}'".format(user , pwd))
    return bool(__cur.rowcount)


def update_stock() :
    bno = int(input("Enter the book number : "))
    __cur.execute("select Book_Name , Available_Stock from stock where Book_No = {}".format(bno))
    data = __cur.fetchall()
    print("Book Name : " , data[0][0])
    print("Available Stock : " , data[0][1])
    stock = int(input("Enter the new stock purchased : "))
    __cur.execute("update stock set Available_Stock = Available_Stock + {}".format(stock))
    print("Updated Successfully")

    
    
