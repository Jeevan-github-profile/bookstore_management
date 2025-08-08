#Discount - Fixed and variable

import mysql.connector

# discount types --- F-Fixed., A-1 to 10 copies, B-10 to 100 copies, C-More than 100 copies

def add_fixed_discount():
    print()
    print("Fixed discount selected:")
    print()
    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()
    
    discount_id=int(input("Enter discount id:"))
    #print("\t\t Discount types: F-Fixed discount, V1-0 to 10 books, V2-10 to 100 books, V3-more than 100 books")
    discount_type='F'
    discount=int(input("Enter discount percentage:"))       
    bookid=int(input("Enter book id:"))

    
    query="insert into discount values({},'{}',{},{})".format(discount_id,discount_type,discount,bookid)
    
    cursor.execute(query)
    con.commit()
    print()
    print("Fixed Discount added successfully")

    return


def add_variable_discount(dtype):
    print()
    print("Variable discount selected:")
    print()

    con=mysql.connector.connect(host="localhost",user="root",passwd="guru123",database="bookstore")
    cursor=con.cursor()

    dicount_id=int(input("Enter discount id:"))
    #print("\t\t Discount types: F-Fixed discount, V1-0 to 10 books, V2-10 to 100 books, V3-more than 100 books")
    if dtype==1:
        discount_type="V1"
    elif dtype==2:
        discount_type="V2"
    elif dtype==3:
        discount_type="V3"
        
    discount=int(input("Enter discount percentage:"))       
    bookid=int(input("Enter book id:"))

    query="insert into discount values({},'{}',{},{})".format(dicount_id,discount_type,discount,bookid)
    
    cursor.execute(query)
    con.commit()

    print()
    print("Variable discount added successfully")
    return
