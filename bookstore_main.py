#bookstore main program

import bookstore.menu as menu
import bookstore.book as book
import bookstore.publisher as publisher
import bookstore.search as search
import bookstore.sales as sales
import bookstore.returns as returns
import bookstore.batchupload as batchupload

def process_book_menu():
    print()
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            book.add_book()
            ch=input("publisherDo you want to add more books (y/n):")
            if ch=="n":
                break
    elif ch==2:
        print()
        print("Modify book details selected:")
        menu.books_modify_menu()
        print()
        mchoice=int(input("Enter your choice:"))
        print()
        if mchoice==1:
            book.modify_book_title()
        elif mchoice==2:
            book.modify_book_price()
        elif mchoice ==3:
            book.modify_publisher()
        elif mchoice==4:
            book.modify_publication_date()
        else:
            print("Wrong choice")

    elif ch==3:
        print("Delete book selected:")
        print()
        book.delete_book()
    elif ch==4:
        print("Set Reorder level:")
        book.set_reorder_level()
    else:
        print("wrong choice:")
        return

def process_publisher_menu():
    print()
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            publisher.add_publisher()
            ch=input("Do you want to add more publisher (y/n):")
            if ch=="n":
                break
    elif ch==2:
        print()
        print("Modify publisher selected:")
        menu.publisher_modify_menu()
        print()
        
        mchoice=int(input("Enter your choice:"))
        print()
        
        if mchoice==1:
            publisher.modify_publisher_name()
        elif mchoice==2:
            publisher.modify_publisher_address()
        else:
            print("Wrong choice")
    elif ch==3:
        print("Delete publisher selected:")
        print()
        publisher.delete_publisher()
    else:
        print("wrong choice:")
        return

'''def process_discount_menu():
    print()
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            discount.add_fixed_discount()
            ch=input("Do you want to add more discount (y/n):")
            if ch=="n":
                break
    elif ch==2:
        print()
        print("Variable discount selected:")
        menu.variable_discount_menu()
        print()
        
        mchoice=int(input("Enter your choice:"))
        print()
        
        if mchoice==1:
            discount.add_variable_discount(1)
        elif mchoice==2:
            discount.add_variable_discount(2)
        elif mchoice==3:
            discount.add_variable_discount(3)
        else:
            print("Wrong choice")
    else:
        print("wrong choice:")
        return
'''

def process_search_menu():
    print()
    ch=int(input("Enter your choice:"))
           
    if ch==1:
        print()
        menu.search_book_menu()
        print()
           
        bchoice=int(input("Enter the choice:"))
        if bchoice==1:
            while True:
                search.search_by_book_id()
                sch=input("Do you want to search again by book id (y/n):")
                if sch=='n':
                    break
        elif bchoice==2:
            while True:
                search.search_by_book_title()
                sch=input("Do you want to search again by book title (y/n):")
                if sch=='n':
                    break
        elif bchoice==3:
            while True:
                search.search_by_publisher_id()
                sch=input("Do you want to search again by publisher id (y/n):")
                if sch=='n':
                    break
        elif bchoice==4:
            while True:
                search.search_by_isbn()
                sch=input("Do you want to search again by isbn (y/n):")
                if sch=='n':
                    break
        elif bchoice==5:
            while True:
                search.search_by_publication_date()
                sch=input("Do you want to search again by publication date (y/n):")
                if sch=='n':
                    break
        elif bchoice==6:
            while True:
                search.search_by_author()
                sch=input("Do you want to search again by author (y/n):")
                if sch=='n':
                    break
        else:
            print("Wrong choice")
    if ch==2:
        print()
        menu.search_publisher_menu()
        print()

        pchoice=int(input("Enter the choice:"))
        if pchoice==1:
            while True:
                search.search_by_pid()
                sch=input("Do you want to search again by publisher id (y/n):")
                if sch=='n':
                    break
        elif pchoice==2:
            while True:
                search.search_by_pname()
                sch=input("Do you want to search again by publisher name (y/n):")
                if sch=='n':
                    break
        else:
            print("Wrong choice")

def process_sales():
    while True:
        sales.add_sales()
        ch=input("Do you want to add more sales (y/n):")
        if ch!='y':
            break

def process_returns():
    while True:
        returns.add_returns()
        ch=input("Do you want to add more returns (y/n):")
        if ch!='y':
            break

def process_upload_menu():
    choice=int(input("Enter your choice:"))
    if choice==1:
        batchupload.publisher_upload()
    elif choice==2:
        batchupload.book_upload()        
    else:
        print("Wrong choice")
        return
        
    
                     
def main():
    while True:
        print()
        menu.main_menu()
        
        print()
        ch=int(input("Enter your choice:"))
        print()
        
        if ch==1:
            menu.book_menu()
            process_book_menu()
        elif ch==2:
            menu.publisher_menu()
            process_publisher_menu()
        elif ch==3:
            print("sales option selected")
            process_sales()
        elif ch==4:
            print("return option selected")
            process_returns()
        elif ch==5:
            menu.discount_menu()
            process_discount_menu()
        elif ch==6:
            menu.search_menu()
            process_search_menu()
        elif ch==7:
            menu.reports_menu()
        elif ch==8:
            menu.upload_menu()
            process_upload_menu()
        else:
            break


#Call main program
main()
