import sys
import time, datetime
from datetime import timedelta
import pandas as pd

# from attr import s
from class_helper import Crud_db

db = Crud_db()

def main():
    # print(print_help())
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        if sys.argv[1] == 'help' or sys.argv[1] == 'h' or sys.argv[1] == 'H':
            print(print_help())

        elif sys.argv[1]=='sginup':
            sginup()

        elif sys.argv[1]=='login':
            login()

        elif sys.argv[1]=='logout':
            logout()

        elif sys.argv[1]=='add_products':
            add_products()

        elif sys.argv[1]=='create_new_bill':
            add_bill()

        elif sys.argv[1]=='update_bill':
            update_bill()

        elif sys.argv[1]=='delete_bill':
            delete_bill()

        elif sys.argv[1]=='add_expence':
            add_expence()

        elif sys.argv[1]=='update_expenses':
            update_expenses()

        elif sys.argv[1]=='delete_expenses':
            delete_expenses()

        elif sys.argv[1]=='print_total_jr':
            if len(sys.argv)==2:
                print_total_jr()
            elif len(sys.argv)==3:
                # the_date = convert_date_format(sys.argv[2])
                print_total_jr(sys.argv[2])


        elif sys.argv[1]== 'save_to_csv':
            if sys.argv[2]==None or sys.argv[2]=='':
                save_to_csv()
            if sys.argv[2]:
                the_date = convert_date_format(sys.argv[2])
                save_to_csv(the_date)
        
        elif sys.argv[1]=='create_pdf_bill':
            save_to_pdf()
        
        else:
            print(print_help())
    elif len(sys.argv) == 1:
        print(print_help())   
    else:
        print('no such command arguments try python project.py help')
        # print(print_help())

def sginup(): # python project.py sginup
    if db.check_if_login() == False:
        db.signup()
    else:
        print('you need to logout first\n use " python project.py logout "')

def login(): # python project.py login
    db.login()

def logout() : # python project.py logout
    db.logout()

def add_products(): # python project.py add_products
    db.add_product()

def add_bill(): # python project create_new_bill
   db.insert_new_bill()

def update_bill(): # python project update_bill
    db.update_bill()


def delete_bill(): # python project.py delete_bill
    db.delete_bill()

def add_expence(): # python project.py add_expence
    db.add_expenses()

def update_expenses(): # python project update_expenses
    db.update_expenses()


def delete_expenses(): # python project.py delete_expenses
    db.delete_expenses()

def print_total_jr(day = None): # python project.py print_total_jr day
    db.print_total_jr(day)

def save_to_csv(day = None): #python project.py save_to_csv day
    db.save_to_csv(day)

def save_to_pdf(): # python project.py create_pdf_bill
    db.save_the_last_bill_to_html_pdf()

def convert_date_format(date):
    the_date = pd.to_datetime(date)
    new_date = the_date.strftime("%Y-%m-%d")
    return new_date
    
    



def print_help(): # python project.py help
    # TODO fix the ortoghraph error
    help_string = ''' 
    This is a Seller Management Systeme that contains many features that allow the seller track his revenue and expenses And register his products with the price and the margin, and register all of this information in a database that  Allow to Create Read Update Delete all the information to manage his selling and expense.

    #### `python project.py help`
    To get help with this project you just type help, that will show you all the command line allowed in this project.

    #### `python project.py sginup` 
    To create a new user with a username and password, a password that is hashed that no one can use your password even if he have access to the database.

    #### `python project.py login`
    To login to your account and register every transaction with your username, it makes you login for 3 hours and automatically logout.

    #### `python project.py logout`
    to logout.

    #### `python project.py create_tables`
    this command creates all the necessary table in the database.

    #### `python project.py add_products`
    this command will add a product name and the price, the margin of this product and if you want, you can add a description for this product 

    #### `python project.py create_new_bill`
    This command will create a new bill for a client all you have to do is to enter the name of the client and the id of the product he buys the number of his products, after that if he buys another product just type yes and continue entering what he buy.

    #### `python project.py update_bill`
    after choosing the bill that you want to update re enter the new products and the bill will be updated 
        
    #### `python project.py delete_bill`
    this command will delete the bill from the general bill and detail bill tables

    #### `python project.py add_expence`
    this command will add a new experience to the database you can add the type of the experiences and if it is for some one you can add his name and the amount of this expense

    #### ` python project update_expenses`
    after choosing the expenses that you want to update reenter the data that will be updated 
        
    #### `python project.py delete_expenses`
    this command will delete the expenses from expenses tables

    #### `python project.py print_total_jr`
    this command will print a table in the terminal window with the total revenue and total expenses and the  difference, if you want to print the hole table add 'all' to like this  "python project.py print_total_jr all"

    #### `python project.py create_pdf_bill`
    This command will create a pdf file and an html file for the last bill you created. 

    #### ` python project.py save_to_csv `
    this command will create a 3 csv file from the tables 'general bill', 'expenses', 'total'
    * If you want to create a CSV file for only a specific day add the date in a format " %Y-%m-%d ". 
    '''
    return help_string



if __name__ == '__main__':
    main()