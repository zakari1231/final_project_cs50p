from class_helper import Crud_db

db = Crud_db()

def main():
    print(print_help())

def sginup(): # python project.py sginup
    if db.check_if_login() == False:
        db.signup()
    else:
        print('you need to logout first\n use " python project.py logout "')

def login(): # python project.py login
    db.login()

def logout() : # python project.py logout
    db.logout()

def add_products(): # python project.py add-products
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

def save_to_csv(day = None): #python project.py save_to_csv
    db.save_to_csv(day)

def save_to_pdf(): #python project.py save_to_pdf
    db.save_the_last_bill_to_html_pdf()
    



def print_help(): # python project.py help
    # TODO fix the ortoghraph error
    help_string = ''' 
    this is a Seller Management Systeme that contain many feateres that allow the seller track his revenue and expenses 
    and register his products with the price and the margin, and register all of this informations in a database that 
    allow to Create Read Update Delete all the information to manage his selling and expense.

     -*- to get help with this project you just type help like this "python project.py help"
        that will show you all the command line allwoed in this project.

     -*- to create a user use the following "python project.py sginup"
        to crate a new user with a username and password, a password that is hashed that no one kan use your password
        even if he have acces to the database.

     -*- if you have an account use the following "python project.py login"
        to login to your account and register every transaction with your username, it make you login for 3 hours and automaticlly logout.

     -*- if you have an account use the following "python project.py logout"
        to logout.

     -*- to create all table in the database use "python project.py create_tables"
        this commande create all the nesessairy table in the database.

     -*- to add new products in the database use "python project.py add_products"
        this commande will add a product name and the price , the margin of this products and if you want you can add a
        descreption for this prodcuts 

     -*- to create new bill for a client use "python project.py create_new_bill"
        this command will create a new bill fro a client all you have to do is to enter the name of the client 
        and the id of the product he buy the number of this product, after that if he buy other product just type yes and
        continue entering what he buy.

     -*- to update a bill use "python project.py update_bill"
        after choosing the bill that you want to update re enter the new products and the bill will be updated 
    
     -*- to delete a bill use "python project.py delete_bill"
        this commande will delete the bill from the general bill and detail bill tables

     -*- to add a new expences use "python project.py add_expence"
        this commande will add a new expence to the database you can add the type of the expences and if it is for somme
        one you can add his name and the ammount of this expenece

     -*- to update an expences use " python project update_expenses"
        after choosing the expences that you want to update re enter the data that will be updated 
    
     -*- to delete a expences use "python project.py delete_expenses"
        this commande will delete the expenses from expnences tables

     -*- to print the total revenue and expences use " python project.py print_total_jr"
        this commande will print a table in the terminal window with the total revenue and total expences and the 
        deferance, if you want to print a total table for a specefec date add the day in a format "%Y-%m-%d" after 
        "python project.py print_total_jr"

     -*- to create a pdf bill for this client use " python project.py create_pdf_bill"
        this command will create a pdf file and an html file for the last bill you created. 

     -*- to create a csv file use " python project.py save_to_csv "
        this command will create a 3 csv file from the tables 'general bill', 'expenses', 'total'
         * if you want to create a csv file for only a specefique day add the date in a fromat " %Y-%m-%d ". 

     '''
    return help_string



if __name__ == '__main__':
    main()