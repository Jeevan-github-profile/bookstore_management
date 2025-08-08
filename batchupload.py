#Batch upload functions

import csv
import mysql.connector

def publisher_upload():
    try:
        fh=open("..\\bookstore\\publisher_upload.csv", "r", newline="")
        preader=csv.reader(fh,delimiter="|")
        next(preader)
    
        con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
        cursor=con.cursor()
        
        count=0
        for record in preader:
            pid=record[0]
            pname=record[1]
            paddress=record[2]

            query="insert into publisher values({},'{}','{}')".format(pid,pname,paddress)
            cursor.execute(query)
            count+=1
        con.commit()

        print()
        print("Publisher batch upload successful")
        print("No. of publishers uploaded:",count)
    except:
        con.rollback()
        print()
        print("An error occurred in Publisher upload.")
        print()


def book_upload():
    try:
        fh=open("..\\bookstore\\book_upload.csv", "r", newline="")
        breader=csv.reader(fh,delimiter="|")
        next(breader)   

        con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
        cursor=con.cursor()

        count=0
        for record in breader:
            bookid=record[0]
            title=record[1]
            isbn=record[2]
            publication_date=record[3]
            author=record[4]
            stock=record[5]
            price=record[6]
            reorder_level=record[7]
            publisher_id=record[8]

            book_query="insert into book values({},'{}','{}', '{}', '{}', {}, {}, {},{})".format(bookid,title,isbn,publication_date,author,stock,price,reorder_level,publisher_id)

            cursor.execute(book_query)
            count+=1
        con.commit()

        print()
        print("Book batch upload successful")
        print("No. of Books uploaded:",count)

    except:
        con.rollback()
        print()
        print("An error occurred in Book upload.")
        print()        

    
    

        
