# Book return entry

from datetime import date
import mysql.connector

import bookstore.book as book
import bookstore.discount as discount


def add_returns():
    print()
    print("Adding returns")
    print()

    items=list()
    total_price=0
    return_item_id=0
    return_id=generate_return_id()
    print("return id:", return_id)

    while True:
        if return_item_id==0:
            return_item_id=generate_return_item_id()
        else:
            return_item_id+=1
        item, price=add_return_detail(return_id,return_item_id)
        items.append(item)
        print(items)
        total_price+=price
        ch=input("Do you want to add more items (y/n):")
        if ch=='n':
            break

    ''' Add return record, return details records, update stock for each return_details record '''
    #Return record addition
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    return_query="insert into returns values({},'{}',{})".format(return_id,date.today(),total_price)

    cursor.execute(return_query)

    #Return details records addition
    for return_item in items:
        i=0
        print(return_item)
        return_item_query="insert into return_detail values({},{},{},{},{})".format(return_item[i][0],return_item[i][1],return_item[i][2],return_item[i][3],return_item[i][4])
        cursor.execute(return_item_query)

        #Update stock for each return detail
        book_stock_query="update book set stock=%s where book_id=%s"
        value=(return_item[i][5],return_item[i][3])
        cursor.execute(book_stock_query,value)
        #increment counter
        i+=1

    con.commit()
    print()
    print("Returns added successfully")
    print()


def add_return_detail(rid,item_id):
    item=list()
    new_stock=0
    price=0

    book_id=int(input("Enter book id:"))

    price=book.get_book_price(book_id)
    #apply discount
    stock=book.get_book_stock(book_id)
    copies=int(input("Enter no.of copies:"))
    new_stock=stock+copies
    
    item.append([item_id,copies, price, book_id,rid,new_stock])

    return item,copies*price
    

def generate_return_id():
    rid=1
    
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    cursor.execute("select return_id from returns")

    data = cursor.fetchall()
    count=cursor.rowcount
    rid=count+1

    return rid

def generate_return_item_id():
    item_id=1
    
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    cursor.execute("select id from return_detail")

    data = cursor.fetchall()
    count=cursor.rowcount
    item_id=count+1

    return item_id
