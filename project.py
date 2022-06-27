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


def print_help(): # python project.py help
    # TODO fix the ortoghraph error
    help_string = ''' 
    this is a Seller Management Systeme that contain many featsers allow the seller track his revenue and expenses and
    register his products with the price and the margin, and register all of this informations in a database that allow 
    to Create Read Update Delete all the information to manage his selling and expense.

     -*- to get help with this project you just type help like this "python project.py help"
        that will show you all the command line allwoed in this project.

     -*- to create a user use the following "python project.py sginup"
        to crate a new user with a username and password, a password that is hashed that no one kan use your password
        even if he have acces to the database.

     -*- if you have an account use the following "python project.py login"
        to login to your account and register every transaction with your username.

     -*- to create all table in the database use "python project.py create_tables"
        this commande create all the nesessairy table in the database.

     -*- to create new bill for a client use "python project.py create_new_bill"
        this command will create a new bill fro a client all you have to do is to enter the name of the client 
        and the id of the product he buy the number of this product, after that if he buy other product just type yes and
        continue entering what he buy.

     -*- to create a pdf bill for this client use " python project.py create_pdf_bill"
        this command will create a pdf file and an html file for the last bill you created. 

     -*- to create a csv file use " python project.py save_to_csv "
        this command will create a 3 csv file from the tables 'general bill', 'expenses', 'total'
         * if you want to create a csv file for only a specefique day add the date in a fromat " %Y-%m-%d ". 

     '''
    return help_string



if __name__ == '__main__':
    main()