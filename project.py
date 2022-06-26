from class_helper import Crud_db

db = Crud_db()

def main():
    print(print_help())

def print_help():
    help_string = ''' 
    this is a seller management systeme it allow the seller to register his products, and whene he buy somthing he
    register this information in a database with the client name and the product that he buy and save it in some kind of
    a bill for the client 
     * to get help with this project you judt type help like this "python project.py help"
     * to create a user user the following "python project.py sginup"
     * if you have an account use the following "python project.py login"

     '''
    return help_string



if __name__ == '__main__':
    main()