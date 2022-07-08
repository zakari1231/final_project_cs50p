import sqlite3
import pandas as pd
import sys
import time, datetime
from datetime import timedelta
import os
# from decorator import check_if_user_login

from werkzeug.security import generate_password_hash, check_password_hash
import getpass

from tabulate import tabulate
from jinja2 import Environment, FileSystemLoader


# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
# import os

# insert the GTK3 Runtime folder at the beginning
# install gtk from link: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')

from weasyprint import HTML, CSS




class Crud_db:
    def __init__(self, database = 'database.db'):
        self.database = database

    def connect(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        # print('connect seccesfully')

    def execute(self, query):
        self.query = query
        self.cursor.execute(self.query)

    def close(self): 
        self.connection.commit()
        self.connection.close()

    def create_tables(self):
        #create users table
        self.connect()
        create_table_users = ''' CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            username VARCHAR NOT NULL, 
            password VARCHAR NOT NULL,
            type_user VARCHAR) '''
        self.execute(create_table_users)
        self.close()
        print("Table users created successfully")

        #create expenses table

        self.connect()
        create_table_expenses = ''' CREATE TABLE IF NOT EXISTS  expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
            type VARCHAR NOT NULL,
            nom VARCHAR,
            montant DECIMAL(100,2) NOT NULL,
            date DATE,
            temp TIME)'''
        self.execute(create_table_expenses)
        self.close()
        print("Table expenses created successfully")

        #create product table

        self.connect()
        create_table_product = ''' CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            product_name TEXT,
            prix REAL,
            margin REAL,
            product_descreption TEXT)'''

        self.execute(create_table_product)
        self.close()
        print("Table product created successfully")

        #create general_bill table

        self.connect()
        create_table_general_bill = ''' CREATE TABLE IF NOT EXISTS general_bill (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            client_name TEXT,
            total REAL,
            total_margin REAL,
            number_of_products INTEGER,
            date_g TEXT,
            time_g TEXT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id))'''

        self.execute(create_table_general_bill)
        self.close()
        print("Table general_bill created successfully")

        #create details_bill table

        self.connect()
        create_table_details_bill = ''' CREATE TABLE IF NOT EXISTS details_bill (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            products INTEGER,
            number_of_products INTEGER,
            prix REAL,
            margin REAL,
            date TEXT,
            time TEXT,
            general_bill_id INTEGER,
            FOREIGN KEY (general_bill_id) REFERENCES general_bill(id),
            FOREIGN KEY (products) REFERENCES product(id))'''

        self.execute(create_table_details_bill)
        self.close()
        print("Table details_bill created successfully")

        self.connect()
        create_table_total = ''' CREATE TABLE IF NOT EXISTS total (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            total_revenu REAL,
            total_margin REAL,
            total_expences REAL,
            total_difference REAL,
            date TEXT UNIQUE)'''

        self.execute(create_table_total)
        self.close()
        print("Table total created successfully")

        self.connect()
        create_table_login_or_not = ''' CREATE TABLE IF NOT EXISTS login_or_not (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            user_id INTEGER,
            date_time_login TEXT,
            date_time_logout TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id))'''

        self.execute(create_table_login_or_not)
        self.close()
        print("Table login_or_not created successfully")


    def chek_if_table_there(self):
        self.connect()
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        self.execute(query)       
        result = self.cursor.fetchall()
        table_result = []
        for row in result:
            table_result.append(row[0])
        print(*table_result, sep=', ')
        if len(result) != 8 :
            print(f'one or more table dose not existe \nthe table in the database are: \n{table_result} ')
        else:
            print(f'the table in the database are: \n {table_result} ')

    
    def insert_new_bill(self):
        if self.check_if_login() == True:
            self.check_if_there_is_products()
            self.connect()
            date_f = str(datetime.date.today())
            # time_f = str(datetime.datetime.now().time())
            time_f = str(datetime.datetime.now().time().strftime("%H:%M:%S"))

            # adding the client name and create a empty general bill that centaine only name of the client and id

            client_name = input('client name: ')
            query01 = 'INSERT INTO general_bill (client_name, date_g, time_g, user_id) VALUES (?, ?, ?, (SELECT user_id FROM login_or_not WHERE date_time_logout = (SELECT MAX(date_time_logout) FROM login_or_not)))'
            data = (client_name,date_f, time_f)
            self.cursor.execute(query01,data) 
            print('added to general bill ..!')
            # add the detail of this bill 
            question = 'yes'
            while question == 'yes':
                product = input('product id: ')
                number_of_product = input('number of product: ')

                date_f2 = str(datetime.date.today())
                time_f2 = str(datetime.datetime.now().time().strftime("%H:%M:%S"))

                query2 = 'INSERT INTO details_bill (products, number_of_products, prix, margin, date,time, general_bill_id) VALUES (?,?,?*(select prix from product where id =?),?*(select margin from product where id =?),?,?,(select max(id) from general_bill where client_name = ?))'
                data_query_2 = (product, number_of_product, number_of_product, product, number_of_product, product, date_f2, time_f2, client_name)
                self.cursor.execute(query2,data_query_2)
                question = input('do you wana add more product for this client (yes/no): ')
            else:
                # after all the detail of this bill added calculat the sum 
                # TODO add a check if id of product in database or not
                query_3 = '''UPDATE general_bill 
                SET total = (SELECT SUM(prix) FROM details_bill WHERE general_bill_id = (select max(id) from general_bill where client_name = ?) ), 
                total_margin = (SELECT SUM(margin) FROM details_bill WHERE general_bill_id = (select max(id) from general_bill where client_name = ?) ),
                number_of_products = (SELECT SUM(number_of_products) FROM details_bill WHERE general_bill_id = (select max(id) from general_bill where client_name = ?) ) 
                WHERE id = (select max(id) from general_bill where client_name = ?)'''
                data_query_3 = (client_name,client_name, client_name, client_name)
                self.cursor.execute(query_3,data_query_3) 
                print(f'all product that |{client_name}| buy added to database seccesfully')
                self.close()
                self.print_the_last_bill()
            self.calculat_total()
        else:
            print('you have to login first to be able to insert a bill')
            self.login()
            self.insert_new_bill()
    
    def update_bill(self):
        date_input = input('do you wana see the bills for this day or for a specific date, if you want for a specific date please entre your date in a format " %Y-%m-%d ": ')
        if date_input == None or date_input == '':
            self.print_general_bill()
        else:
            self.print_general_bill(date_input)
        the_id = input('please choose the id of the bill you want to change: ')
        self.print_the_last_bill(the_id)
        self.connect()
        delete_query = ''' DELETE FROM  details_bill WHERE general_bill_id = ?'''
        id_data = (the_id,)
        self.cursor.execute(delete_query,id_data)
        # self.close()

        print(f'Now please update the detail for the bill with the id = {the_id}')
        question = 'yes'
        while question == 'yes':
            product = input('product id: ')
            number_of_product = input('number of product: ')

            date_f = str(datetime.date.today())
            time_f = str(datetime.datetime.now().time().strftime("%H:%M:%S"))

            query2 = 'INSERT INTO details_bill (products, number_of_products, prix, margin, date,time, general_bill_id) VALUES (?,?,?*(select prix from product where id =?),?*(select margin from product where id =?),?,?,?)'
            data_query_2 = (product, number_of_product, number_of_product, product, number_of_product, product, date_f, time_f, the_id)
            self.cursor.execute(query2,data_query_2)
            question = input('do you wana add more product for this client (yes/no): ')
        else:
            # after all the detail of this bill added calculat the sum 
            # TODO add a check if id of product in database or not
            query_3 = '''UPDATE general_bill 
            SET total = (SELECT SUM(prix) FROM details_bill WHERE general_bill_id = ?), 
            total_margin = (SELECT SUM(margin) FROM details_bill WHERE general_bill_id = ? ),
            number_of_products = (SELECT SUM(number_of_products) FROM details_bill WHERE general_bill_id = ? ) 
            WHERE id = ?'''
            data_query_3 = (the_id,the_id, the_id, the_id)
            self.cursor.execute(query_3,data_query_3) 
            self.close()
            self.print_the_last_bill(the_id)
        self.calculat_total()


    def delete_bill(self, id = None):
        if id:
            the_id = id
        else:
            the_id = input('please enter the id of the bill you want to delete: ')
        
        self.connect()
        data_id = (the_id,)
        query_delete_detail_bill = ''' DELETE FROM details_bill WHERE general_bill_id = ?'''
        query_delete_general_bill = ''' DELETE FROM  general_bill WHERE id = ?'''
        self.cursor.execute(query_delete_detail_bill, data_id)
        self.cursor.execute(query_delete_general_bill, data_id)
        self.close()
        print(f'bill with the id = {the_id} has been deleted successfully')
        self.calculat_total()

    
    def add_expenses(self):
        self.connect()
        type_expenses = input('enter the type of the expense: ')
        name = input('is this expense for some one? if yes type his name : ')
        montant = float(input('how much dose it cost: '))
        date_f = str(datetime.date.today())
        # time_f = str(datetime.datetime.now().time())
        time_f = str(datetime.datetime.now().time().strftime("%H:%M:%S"))
        query_expenses = 'INSERT INTO expenses (type, nom, montant, date, temp) VALUES (?,?,?,?,?)'
        data_expenses = (type_expenses, name, montant, date_f, time_f)
        self.cursor.execute(query_expenses,data_expenses)
        print('expense added to database seccesfully')
        self.close()
        self.calculat_total()
    
    def update_expenses(self):
        the_day = input('if you want to update an expence in a specific date please enter the date in a format " %Y-%m-%d ": ')
        if the_day == None or the_day == '':
            self.print_expences_for_day()
        else:
            self.print_expences_for_day(the_day)

        the_expence_id = input('please choose the id of the expence you want to change: ')
        self.print_last_expences(the_expence_id)
        self.connect()
        type_expenses = input('enter the type of the expense: ')
        name = input('is this expense for some one? if yes type his name : ')
        montant = float(input('how much dose it cost: '))
        query_update_expence = ''' UPDATE expenses SET type=?, name=?, montant=? WHERE id=? '''
        data = (type_expenses, name, montant, the_expence_id)
        self.cursor.execute(query_update_expence,data)
        self.close()
        print(f'expence with the id = {the_expence_id} has been updated successfully')
        self.print_last_expences(the_expence_id)
        self.calculat_total()


    def delete_expenses(self, id = None):
        if id:
            the_id = id
        else:
            the_id = input('please enter the id of the expence you want to delete: ')
        
        query_delete_expence = ''' DELETE FROM expenses WHERE id = ? '''
        data_id = (the_id,)
        self.cursor.execute(query_delete_expence, data_id)
        self.close()
        print(f'expenses with the id = {the_id} has been deleted successfully')
        self.calculat_total()
    

    def calculat_total(self, day = None):
        # TODO make calculat_total work in every method whatever the date is not just the today
        self.connect()
        if day == None or day == '':
            date_f = str(datetime.date.today())
        else:
            date_f = day

        first_query = 'INSERT INTO total (date) VALUES (?) ON CONFLICT (date) DO NOTHING'
        data_total_1 = (date_f,)
        self.cursor.execute(first_query, data_total_1)
        self.close()
        self.connect()
        query_2 = '''UPDATE total 
        SET total_revenu = (SELECT SUM(total) FROM general_bill WHERE date_g = ?), 
        total_margin= (SELECT SUM(total_margin) FROM general_bill WHERE date_g = ?), 
        total_expences = (SELECT SUM(montant) FROM expenses WHERE date = ?),
        total_difference = ((SELECT SUM(total_margin) FROM general_bill WHERE date_g = ?)-(SELECT SUM(montant) FROM expenses WHERE date = ?)) 
        WHERE date = ?'''
        data_query_2 = (date_f,date_f,date_f, date_f,date_f, date_f)
        self.cursor.execute(query_2, data_query_2)
        self.close()
        # self.print_total_jr()

    def add_product(self):
        self.connect()
        product_name = input('product name: ')
        prix = float(input('the price : '))
        margin = float(input('profit: '))
        product_discreption = input('discreption: ')
        product_query = 'INSERT INTO product (product_name, prix, margin, product_descreption) VALUES (?,?,?,?)'
        data_set = [product_name,prix,margin,product_discreption]
        self.cursor.execute(product_query,data_set) 
        self.close()
        print(f'product {product_name} added to database')
        question = input('do you wana add more products ?(yes/no): ')
        if question.lower() == 'yes':
            self.add_product()
        else:
            pass
    
    def check_if_there_is_products(self):
        self.connect()
        query_table = ''' SELECT id,product_name, prix, margin, product_descreption FROM product '''
        self.cursor.execute(query_table)
        result = self.cursor.fetchall()
        if result:
            self.print_product_table()
        else:
            print('you have to add products first')
            self.add_product()
        ...


    def signup(self):
        while True:
            username = input('please entre a new username: ')
            self.connect()
            username_query = 'SELECT username FROM users WHERE username = ?'
            username_data = (username,)
            self.cursor.execute(username_query,username_data)
            result = self.cursor.fetchone()
            if result:
                print('username alaredy exists please try another one')
            else:
                break

        while True:
            password = getpass.getpass('Password:')
            repeat_password = getpass.getpass('type your Password Again:')
            if password !=repeat_password:
                continue
            else:
                break

        hashed_pass = generate_password_hash(password, method='sha256')
        query_signup = 'INSERT INTO users (username, password) VALUES (?,?)'
        data_signup = (username, hashed_pass)
        self.cursor.execute(query_signup,data_signup) 
        self.close()
        self.connect()
        query_user_check_login = 'INSERT INTO login_or_not (user_id) VALUES ((SELECT id FROM users WHERE username = ?))'
        data_user_check = (username,)
        self.cursor.execute(query_user_check_login,data_user_check) 
        print('user added to database successfully ...')
        self.close()

    def login(self):
        if self.check_if_login() == True:
            sys.exit('you are logged in')
        else:
            atempts = 4
            while atempts !=0:
                the_username = input('enter your username: ')
                the_password = getpass.getpass('enter your password: ')
                self.connect()
                query_login = 'SELECT username, password FROM users WHERE username = ?'
                username_data = (the_username,)
                self.cursor.execute(query_login,username_data)
                result = self.cursor.fetchone()
                if check_password_hash(result[1], the_password) == True:
                    print('login successfully')
                    date_time_login = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    time_to_logout = datetime.datetime.now() + timedelta(hours=3)
                    date_time_logout = str(time_to_logout.strftime("%Y-%m-%d %H:%M:%S"))
                    query_check_login = 'UPDATE login_or_not SET date_time_login = ?, date_time_logout = ? WHERE user_id = (SELECT id FROM users WHERE username = ?)'                    
                    data_check_login = (date_time_login, date_time_logout, the_username,)
                    self.cursor.execute(query_check_login, data_check_login)
                    self.close()
                    break

                else:
                    atempts -=1
                    print('wrong username or password please try again')
                    print(f'you have only {atempts} Attempts')
            else:
                sys.exit('sorry you have to try another time')
                
    def logout(self):
        if self.check_if_login() == False:
            print('you have to login first in order to to be able to logout')
        else:
            self.connect()
            new_date_time_logout = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            query_logout = ''' UPDATE login_or_not SET date_time_logout = ? WHERE date_time_logout = (SELECT MAX(date_time_logout) FROM login_or_not)'''
            data_logout = (new_date_time_logout,)
            self.cursor.execute(query_logout, data_logout)
            self.close()
            print('you are loggout successfully')


    def check_if_login(self):
        self.connect()
        query_check = 'SELECT date_time_login, max(date_time_logout) FROM login_or_not'
        self.cursor.execute(query_check)
        result = self.cursor.fetchone()
        if result[0]==None:
            return False
        else:
            date_time_now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            date_time_logout = result[1]
            if date_time_now > date_time_logout:
                return False
            elif date_time_now < date_time_logout:
                return True

    def print_product_table(self):
        """ this fucntion print the table of all product as a table in terminal for the user to chose the product befor adding to new bill, by selectin table products and return all product and use the liberery tabulate to change this result into a table in the terminal """

        self.connect()
        query_table = ''' SELECT id,product_name, prix, margin, product_descreption FROM product '''
        table_headers = ['id','product name', 'prix', 'margin', 'product descreption']
        self.cursor.execute(query_table)
        result = self.cursor.fetchall()
        print(tabulate(result, headers=table_headers, tablefmt="psql")) #for another table user tablefmt="grid"
    
    def print_general_bill(self, day = None):
        if day == None:
            self.connect()
            date_n = str(datetime.date.today())
            query_general_bill = ''' SELECT general_bill.id, general_bill.client_name , general_bill.total , general_bill.total_margin , general_bill.number_of_products , general_bill.date_g ,general_bill.time_g , users.username user_id 
                FROM general_bill join users 
                on general_bill.user_id = users.id
                WHERE general_bill.date_g= ? '''
            date_data = (date_n,)
            self.cursor.execute(query_general_bill, date_data)
            tabel_generalbill_headers = ['id','client name', 'total', 'total_marigin', 'number of product', 'date','time', 'user']
            result = self.cursor.fetchall()     
            print(tabulate(result, headers=tabel_generalbill_headers, tablefmt="psql"))
        if day:
            self.connect()
            # date_n = str(datetime.date.today())
            the_date = str(day.strftime("%Y-%m-%d"))
            query_general_bill = ''' SELECT general_bill.id, general_bill.client_name , general_bill.total , general_bill.total_margin , general_bill.number_of_products , general_bill.date_g ,general_bill.time_g , users.username user_id 
                FROM general_bill join users 
                on general_bill.user_id = users.id
                WHERE general_bill.date_g= ? '''
            date_data = (the_date)
            self.cursor.execute(query_general_bill, date_data)
            tabel_generalbill_headers = ['id','client name', 'total', 'total_marigin', 'number of product', 'date','time', 'user']
            result = self.cursor.fetchall()     
            print(tabulate(result, headers=tabel_generalbill_headers, tablefmt="psql"))


    def print_the_last_bill(self, id = None):
        # TODO make this fucntion work but less lines
        if id == None:
            self.connect()
            query_general_bill = ''' SELECT general_bill.id, general_bill.client_name , general_bill.total , general_bill.total_margin , general_bill.number_of_products , general_bill.date_g ,general_bill.time_g , users.username user_id 
            FROM general_bill join users 
            on general_bill.user_id = users.id
            WHERE general_bill.id=(SELECT MAX(id) FROM general_bill) '''
            self.cursor.execute(query_general_bill)
            tabel_generalbill_headers = ['id','client name', 'total', 'total_marigin', 'number of product', 'date','time', 'user'] 
            result = self.cursor.fetchall()     
            print(tabulate(result, headers=tabel_generalbill_headers, tablefmt="psql")) #for another table user tablefmt="grid"

            query_details_bill = ''' SELECT product.product_name products, details_bill.number_of_products, details_bill.prix, details_bill.margin, details_bill.date, details_bill.time 
            FROM details_bill join product
            on product.id = products
            WHERE details_bill.general_bill_id = (SELECT MAX(id) FROM general_bill)'''
            headers_detail_bill = ['product name', 'number of products', 'price', 'margin', 'date', 'time']
            self.cursor.execute(query_details_bill)
            result_detail_bill = self.cursor.fetchall() 
            print(tabulate(result_detail_bill, headers=headers_detail_bill, tablefmt="psql")) #for another table user tablefmt="grid"
        if id:
            self.connect()
            query_general_bill = ''' SELECT general_bill.id, general_bill.client_name , general_bill.total , general_bill.total_margin , general_bill.number_of_products , general_bill.date_g ,general_bill.time_g , users.username user_id 
            FROM general_bill join users 
            on general_bill.user_id = users.id
            WHERE general_bill.id= ? '''
            data_id = (id,)
            self.cursor.execute(query_general_bill,data_id)
            tabel_generalbill_headers = ['id','client name', 'total', 'total_marigin', 'number of product', 'date','time', 'user'] 
            result = self.cursor.fetchall()     
            print(tabulate(result, headers=tabel_generalbill_headers, tablefmt="psql")) #for another table user tablefmt="grid"

            query_details_bill = ''' SELECT product.product_name products, details_bill.number_of_products, details_bill.prix, details_bill.margin, details_bill.date, details_bill.time 
            FROM details_bill join product
            on product.id = products
            WHERE details_bill.general_bill_id = ?'''
            headers_detail_bill = ['product name', 'number of products', 'price', 'margin', 'date', 'time']
            self.cursor.execute(query_details_bill,data_id)
            result_detail_bill = self.cursor.fetchall() 
            print(tabulate(result_detail_bill, headers=headers_detail_bill, tablefmt="psql")) #for another table user tablefmt="grid"


    def print_last_expences(self, id = None):
        self.connect()
        if id == None:
            query_expences = ''' SELECT * FROM expenses WHERE id = (SELECT MAX(id) FROM expenses)'''
            self.cursor.execute(query_expences)
        else :
            query_expences = ''' SELECT * FROM expenses WHERE id = ?'''
            data_id = (id,)
            self.cursor.execute(query_expences, data_id)
        headers_expences = ['id', 'type', 'name', 'montant', 'date','time']
        result_expences = self.cursor.fetchall() 
        print(tabulate(result_expences, headers=headers_expences, tablefmt="psql")) #for another table user tablefmt="grid"

    def print_expences_for_day(self, day = None):
        if day == None:
            the_date = str(datetime.date.today())
        else:
            the_date = input('please entre your date in a format " %Y-%m-%d ": ')
        self.connect()
        query_expences = ''' SELECT * FROM expenses WHERE date = ?'''
        data_date = (the_date,)
        self.cursor.execute(query_expences, data_date)
        result = self.cursor.fetchall() 
        headers_expences = ['id', 'type', 'name', 'montant', 'date','time']
        print(tabulate(result, headers=headers_expences, tablefmt="psql")) #for another table user tablefmt="grid"
        pass

    def print_total_jr(self, day = None):
        query_total = ''' SELECT * FROM total WHERE date = (SELECT MAX(date) FROM total) '''
        query_total_all = ''' SELECT * FROM total '''
        header_total = ['id', 'total revenu', 'total margin', 'total expences','difference', 'date']
        if day == None:
            self.connect()
            self.cursor.execute(query_total)
            result_total = self.cursor.fetchall()
            print(tabulate(result_total, headers=header_total, tablefmt="psql")) #for another table user tablefmt="grid"
        if day == 'all':
            self.connect()
            self.cursor.execute(query_total_all)
            result_total_all = self.cursor.fetchall()
            print(tabulate(result_total_all, headers=header_total, tablefmt="psql")) #for another table user tablefmt="grid"

    def save_to_csv(self, day = None):
        if day == None:
            query_general_bill_all = ''' SELECT * FROM  general_bill'''
            query_expences_all = ''' SELECT * FROM expenses '''
            query_total_all = ''' SELECT * FROM total '''

            df1 = pd.read_sql(query_general_bill_all, sqlite3.connect(self.database))
            df1.to_csv('general_bill_all.csv', index = False)

            df2 = pd.read_sql(query_expences_all, sqlite3.connect(self.database))
            df2.to_csv('expenses_all.csv', index = False)

            df3 = pd.read_sql(query_total_all, sqlite3.connect(self.database))
            df3.to_csv('total_day_all.csv', index = False)
        if day :
            try:
                day = str(day)
                query_general_bill_all = f" SELECT * FROM  general_bill WHERE date_g == '{day}'"
                query_expences_all = f' SELECT * FROM expenses WHERE date == "{day}" '
                query_total_all = f' SELECT * FROM total WHERE date == "{day}" '

                df1 = pd.read_sql(query_general_bill_all, sqlite3.connect(self.database))
                # print(df1)
                df1.to_csv(f'general_bill_{day}.csv', index = False)

                df2 = pd.read_sql(query_expences_all, sqlite3.connect(self.database))
                df2.to_csv(f'expenses_{day}.csv', index = False)

                df3 = pd.read_sql(query_total_all, sqlite3.connect(self.database))
                df3.to_csv(f'total_day_{day}.csv', index = False)
            except ValueError:
                sys.exit('value Error')

    def save_the_last_bill_to_html_pdf(self):
        env = Environment(loader=FileSystemLoader('templates'))
        # 3. Load the template from the Environment
        template = env.get_template('th_bill.html')

        # retrive the last general bill and details bill
        self.connect()
        query_general_bill = ''' SELECT general_bill.id, general_bill.client_name , general_bill.total , general_bill.total_margin , general_bill.number_of_products , general_bill.date_g ,general_bill.time_g , users.username user_id 
        FROM general_bill join users 
        on general_bill.user_id = users.id
        WHERE general_bill.id=(SELECT MAX(id) FROM general_bill) '''
        self.cursor.execute(query_general_bill)
        result_general_bill = self.cursor.fetchall()
        # print(result_general_bill)

        #  retrive the detail bill 

        query_details_bill = ''' SELECT product.product_name products, details_bill.number_of_products, details_bill.prix, details_bill.margin, details_bill.date, details_bill.time 
        FROM details_bill join product
        on product.id = products
        WHERE details_bill.general_bill_id = (SELECT MAX(id) FROM general_bill)'''
        self.cursor.execute(query_details_bill)
        result_detail_bill = self.cursor.fetchall() 
        # print(result_detail_bill)

        html = template.render(result_general = result_general_bill,
                            result_detail_bill = result_detail_bill)

        with open('html_report_jinja.html', 'w') as f:
            f.write(html)

        css = CSS(string='''
            @page {size: A4; margin: 1cm;} 
            th, td {border: 1px solid black;}
            ''')
        HTML('html_report_jinja.html').write_pdf('weasyprint_pdf_report.pdf', stylesheets=[css])
        print('pdf file and html file created successfully')

        if os.path.exists("html_report_jinja.html"):
            os.remove("html_report_jinja.html")
            print("The file has been deleted successfully")
        else:
            print("The file does not exist!")


        





db = Crud_db()

# db.create_tables()
# check_if_user_login(db.check_if_login(), db.login())
#db.chek_if_table_there()
# db.insert_new_bill()
# db.add_expenses()
# db.signup()
# db.login()
# db.logout()
# db.check_if_login()
# db.add_product()
# db.calculat_total()
# db.update_bill()

# db.save_to_csv()
# db.save_the_last_bill_to_html_pdf()

# db.print_product_table()
# db.print_the_last_bill()
# db.print_last_expences()
# db.print_total_jr('all')

# def from_csv_to_table(filename):
#     #header = []
#     table = []
#     with open(filename) as file:
#         reader = csv.reader(file)
#         header =next(reader)
#         for row in reader:
#             table.append(row)
#     return (tabulate(table, header, tablefmt="grid"))