#Books Inventory related functions

import mysql.connector

def getbook():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    bookid=int(input("Enter book id:"))

    query="select * from book where "
    
def add_book():
    print()
    print("add book")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    bookid=int(input("Enter book id:"))
    title=input("Enter Title:")
    isbn=input("Enter ISBN:")
    publication_date=input("Enter publication date:")
    author=input("Enter author name:")
    stock=int(input("Enter stock:"))
    price=int(input("Enter price:"))
    reorder_level=int(input("Enter reorder level:"))
    publisher_id=int(input("Enter publisher id:"))                 
                      
    query="insert into book values({},'{}','{}', '{}', '{}', {}, {}, {},{})".format(bookid,title,isbn,publication_date,author,stock,price,reorder_level,publisher_id)

    cursor.execute(query)
    con.commit()
    print("Row inserted")

def modify_book_title():
    print()
    print("modify book title")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    bookid=int(input("Enter book id:"))
    title=input("Enter new title:")
    query="update book set title=%s where book_id=%s"
    value=(title,bookid)
    cursor.execute(query,value)
    con.commit()
    print()
    print("Book title modified successfully")
    return

def modify_book_price():
    print()
    print("modify book price")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    bookid=int(input("Enter book id:"))
    price=int(input("Enter new price:"))
    query="update book set price=%s where book_id=%s"
    value=(price,bookid)
    cursor.execute(query,value)
    con.commit()
    print()
    print("book price modified successfully")    
    return

def modify_publisher():
    print()
    print("modify book publisher")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    bookid=int(input("Enter book id:"))
    pid=input("Enter new publisher id:")
    query="update book set pub_id=%s where book_id=%s"
    value=(pid,bookid)
    cursor.execute(query,value)
    con.commit()
    print()
    print("publisher modified successfully")
    return

def modify_publication_date():
    print()
    print("modify publication date")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    bookid=int(input("Enter book id:"))
    pdate=input("Enter new publication date:")
    query="update book set publication_date=%s where book_id=%s"
    value=(pdate,bookid)
    cursor.execute(query,value)
    con.commit()
    print()
    print("publication date modified successfully")    
    return

def delete_book():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    print()
    bookid=int(input("Enter book id:"))

    query="delete from book where book_id=%s"
    value=(bookid,)
    cursor.execute(query,value)
    con.commit()
    print()
    print("Book deleted successfully")
    return

    

def set_reorder_level():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    print()
    bookid=int(input("Enter book id:"))
    reorderlevel=int(input("Enter reorder level:"))

    query="update book set reorder_level=%s where book_id=%s"
    value=(reorderlevel,bookid)
    cursor.execute(query,value)
    con.commit()
    print()
    print("Reorder level set successfully")    
    return


def get_book_price(book_id):
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    query="select price from book where book_id=%s"
    value=(book_id,)
    cursor.execute(query,value)
    data=cursor.fetchone()
    print("price:",data[0])
    return int(data[0])

def get_book_stock(book_id):
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    query="select stock from book where book_id=%s"
    value=(book_id,)
    cursor.execute(query,value)
    data=cursor.fetchone()
    print("stock:",data[0])
    return int(data[0])
