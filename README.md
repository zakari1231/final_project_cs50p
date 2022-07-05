# selling management system
#### Video Demo:  <URL HERE>
#### Description:

This is a Seller Management Systeme that contains many features that allow the seller track his revenue and expenses And register his products with the price and the margin, and register all of this information in a database that  Allow to Create Read Update Delete all the information to manage his selling and expense.

# Project Features

* in this project we create a class that deal with all the thing nessecairy to make a CRUD application(Create, Read, Update and Delete), 

we use a few laberey in this project that help facilite and not reenvente the weell like:
- `sqlite3` allows accessing the database using a nonstandard variant of the SQL query language.
- `datetime` that help get the date and time in any format we want and also make it easy to handel the manipulation in time or date.
- `panda` that help transform a sql query to a csv file in more effecent an easy way 
- `getpass` labreery that help to hide the passwrod whene the user want to login or sginup.
- `werkzeug` labrery that help encrypte the password.
- `jinja2` that helpt create html pages and `weasyprint` convert that html page into pdf file.
- `tabulate` that print tables 

this class initially create a database in a sqlite and have a methode to connect to that database and to execute query, 
we create all the table nessecaery for this project using sql query for exemple:
```
''' CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            username VARCHAR NOT NULL, 
            password VARCHAR NOT NULL,
            type_user VARCHAR) '''
```
this query create a table for the users, with taht every user have an id, username, password and the type of user

## Products

after adding somme products you can see them in a form of a table in terminal window like this 
![Products](/screenshots/1.png) 

## bill

adding a bill is very easy all you have to to is enter the client name and the product he buy and the number of that product and after that the class print the bill in form of 2 table in the terminal window like this 
![bill](/screenshots/2.png)

## expences

any selling management system must have a way to enter the income and the expences and like the bill whene you enter the expences you can see it in a form of table in terminal window like this 
![expences](/screenshots/3.png)

## total 
after adding an expences or a bill the program calculat automattcly the total expences and the total income and the total diffrences and the total number of productes and of corse print them in a form of table like this 
![total](/screenshots/4.png)

## save your daily report as a csv file
you can save 3 csv file of the income and expences and the total of any day and every day registered in the database

## save the last bill to a pdf file
you can also save the last bill to a pdf file like this 
![save the last bill to a pdf file](/screenshots/5.png)

to run this project first you need to install all the requirements using 
```
pip install -r requirements.txt
```

and then use one of this command 

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
this command will print a table in the terminal window with the total revenue and total expenses and the  difference, if you want to print a total table for a specific date, add the day in a format "%Y-%m-%d" after "python project.py print_total_jr"

#### `python project.py create_pdf_bill`
This command will create a pdf file and an html file for the last bill you created. 

#### ` python project.py save_to_csv `
this command will create a 3 csv file from the tables 'general bill', 'expenses', 'total'
* If you want to create a CSV file for only a specific day add the date in a format " %Y-%m-%d ". 

finally 

Huge thanks to David J. Malan and team for making this awsome courses 