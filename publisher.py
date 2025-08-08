#Publisher related functions

import mysql.connector

def add_publisher():
    print()
    print("Add publisher selected:")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    pid=int(input("Enter publisher id:"))
    pname=input("Enter publisher name:")
    paddress=input("Enter publisher address:")
    
    query="insert into publisher values({},'{}','{}')".format(pid,pname,paddress)
    
    cursor.execute(query)
    con.commit()
    print("Publisher inserted successfully")


def modify_publisher_name():
    print()
    print("modify publisher name")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    pid=int(input("Enter publisher id:"))
    pname=input("Enter new publisher name:")
    query="update publisher set publisher_name=%s where publisher_id=%s"
    value=(pname,pid)
    cursor.execute(query,value)
    con.commit()
    print()
    print("Publisher name modified successfully")
    return

    
def modify_publisher_address():
    print()
    print("modify publisher address")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    pid=int(input("Enter publisher id:"))
    paddress=input("Enter new publisher address:")
    query="update publisher set address=%s where publisher_id=%s"
    value=(paddress,pid)
    cursor.execute(query,value)
    con.commit()
    print()
    print("Publisher address modified successfully")
    return

def delete_publisher():
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    print()
    pid=int(input("Enter publisher id:"))

    query="delete from publisher where publisher_id=%s"
    value=(pid,)
    cursor.execute(query,value)
    con.commit()
    print()
    print("Publisher deleted successfully")
    return
