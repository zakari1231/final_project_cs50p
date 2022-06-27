from class_helper import Crud_db

db = Crud_db()

def main():
    print(print_help())

def print_help():
    # TODO fix the ortoghraph error
    help_string = ''' 
    this is a Seller Management Systeme that contain many featsers allow the seller track his revenue and expenses and
    register his products with the price and the margin, and register all of this informations in a database that allow to Create Read Update Delete all the information to manage his selling and expense.

     -*- to get help with this project you just type help like this "python project.py help"
        that will show you all the command line allwoed in this project.

     -*- to create a user use the following "python project.py sginup"
        to crate a new user with a username and password, a password that is hashed that no one kan use your password
        even if he have acces to the database.

     -*- if you have an account use the following "python project.py login"
        to login to your account and register every transaction with your username.

     -*- to create all table in the database use "python project.py create_tables"
        this commande create all the nesessairy table in the database.

     '''
    return help_string



if __name__ == '__main__':
    main()