# Book sales entry

from datetime import date
import mysql.connector

import bookstore.book as book
import bookstore.discount as discount


def add_sales():
    print()
    print("Adding sales")
    print()

    items=list()
    total_price=0
    sale_item_id=0
    sale_id=generate_sale_id()
    print("sale id:", sale_id)

    while True:
        if sale_item_id==0:
            sale_item_id=generate_sale_item_id()
        else:
            sale_item_id+=1
        item, price=add_sale_detail(sale_id,sale_item_id)
        items.append(item)
        print(items)
        total_price+=price
        ch=input("Do you want to add more items (y/n):")
        if ch=='n':
            break

    ''' Add sale record, sale details records, update stock for each sale_details_record '''
    #Sale record addition
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    sale_query="insert into sales values({},'{}',{})".format(sale_id,date.today(),total_price)

    cursor.execute(sale_query)

    #Sale details records addition
    for sale_item in items:
        i=0
        print(sale_item)
        sale_item_query="insert into sale_detail values({},{},{},{},{})".format(sale_item[i][0],sale_item[i][1],sale_item[i][2],sale_item[i][3],sale_item[i][4])
        cursor.execute(sale_item_query)

        #Update stock for each sale detail
        book_stock_query="update book set stock=%s where book_id=%s"
        value=(sale_item[i][5],sale_item[i][3])
        cursor.execute(book_stock_query,value)
        #increment counter
        i+=1

    con.commit()
    print()
    print("Sales added successfully")
    print()


def add_sale_detail(sid,item_id):
    item=list()
    new_stock=0
    price=0

    book_id=int(input("Enter book id:"))

    price=book.get_book_price(book_id)
    #apply discount
    stock=book.get_book_stock(book_id)
    copies=int(input("Enter no.of copies:"))
    new_stock=stock-copies
    
    item.append([item_id,copies, price, book_id,sid,new_stock])

    return item,copies*price
    

def generate_sale_id():
    sid=1
    
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    cursor.execute("select sale_id from sales")

    data = cursor.fetchall()
    count=cursor.rowcount
    sid=count+1

    return sid

def generate_sale_item_id():
    item_id=1
    
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    cursor.execute("select id from sale_detail")

    data = cursor.fetchall()
    count=cursor.rowcount
    item_id=count+1

    return item_id
