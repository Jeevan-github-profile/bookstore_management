# Search functionality

import mysql.connector

''' Book Search features '''
def search_by_book_id():
    
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    print()
    bookid=int(input("Enter book id:"))
    print()
    
    query="select * from book where book_id=%s"
    value=(bookid,)
    cursor.execute(query,value)

    data=cursor.fetchone()

    count=cursor.rowcount
    if count==0:
        print("No books found")
    else:
        print(data)
    print()    
    return


def search_by_book_title():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    
    print()
    book_title=input("Enter book title:")
    print()

    query="select * from book where title=%s"
    value=(book_title,)
    cursor.execute(query,value)

    data=cursor.fetchall()

    count=cursor.rowcount
    if count==0:
        print("No books found")
    else:
        for row in data:
            print(row)
    print()    

    return

def search_by_publisher_id():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    
    print()
    pid=int(input("Enter publisher id:"))
    print()

    query="select * from book where publisher_id=%s"
    value=(pid,)
    cursor.execute(query,value)

    data=cursor.fetchall()

    count=cursor.rowcount
    if count==0:
        print("No books found")
    else:
        for row in data:
            print(row)
    print()    

    return

def search_by_isbn():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    
    print()
    isbn=input("Enter ISBN:")
    print()

    query="select * from book where isbn=%s"
    value=(isbn,)
    cursor.execute(query,value)

    data=cursor.fetchone()

    count=cursor.rowcount
    if count==0:
        print("No books found")
    else:
        print(data)
    print()    
    return

def search_by_publication_date():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    
    print()
    pdate=input("Enter publication date:")
    print()

    query="select * from book where publication_date=%s"
    value=(pdate,)
    cursor.execute(query,value)

    data=cursor.fetchall()

    count=cursor.rowcount
    if count==0:
        print("No books found")
    else:
        for row in data:
            print(row)
    print()     
    return

def search_by_author():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    
    print()
    author=input("Enter author:")
    print()

    query="select * from book where author=%s"
    value=(author,)
    cursor.execute(query,value)

    data=cursor.fetchall()

    count=cursor.rowcount
    if count==0:
        print("No books found")
    else:
        for row in data:
            print(row)
    print()
    
    return


''' Publisher search feature '''

def search_by_pid():
    
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    print()
    pid=int(input("Enter publisher id:"))
    print()
    
    query="select * from publisher where publisher_id=%s"
    value=(pid,)
    cursor.execute(query,value)

    data=cursor.fetchone()

    count=cursor.rowcount
    if count==0:
        print("No Publisher found")
    else:
        print(data)
    print()    
    return

def search_by_pname():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    print()
    pname=input("Enter publisher name:")
    print()
    
    query="select * from publisher where publisher_name=%s"
    value=(pname,)
    cursor.execute(query,value)

    data=cursor.fetchall()

    count=cursor.rowcount
    if count==0:
        print("No publisher found")
    else:
        for row in data:
            print(row)
    print()
    return
