# selling management system
#### Video Demo:  
<a href="http://www.youtube.com/watch?feature=player_embedded&v=nTQUwghvy5Q" target="_blank">
 <img src="http://img.youtube.com/vi/nTQUwghvy5Q/mqdefault.jpg" alt="Watch the video" width="240" height="180" border="10" />
</a>
<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/5IyFgu6zvdM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->

<!-- [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/5IyFgu6zvdM/0.jpg)](https://www.youtube.com/watch?v=5IyFgu6zvdM) -->
<!-- <URL HERE> -->
#### Description:

This is a Seller Management Systeme that contains many features that allow the seller track his revenue and expenses And register his products with the price and the margin, and register all of this information in a database that  Allow to Create Read Update Delete all the information to manage his selling and expense.

# Project Features

* in this project we create a class that deals with all the thing necessary to make a CRUD application (Create, Read, Update and Delete), 

we use a few libraries in this project that help facilities and not reinventing the Wheel in a manner of speaking like:
- `sqlite3` Allows accessing the database using a nonstandard variant of the SQL query language.
- `datetime` That helps get the date and time in any format we want and also make it easy to handle the manipulation in time or date.
- `panda` That helps transform a SQL query to a CSV file in more efficient an easy way. 
- `getpass` A library that helps to hide the password when the user want to login or sginup.
- `werkzeug` A library that helps encrypt the password.
- `jinja2` that helpe create html pages and `weasyprint` To convert that html page into a pdf file.
- `tabulate` that print tables 

This class initially creates a database in a cyclist and have a method to connect to that database and to execute query, 
We create all the table necessary for this project using SQL query for example:
```
''' CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            username VARCHAR NOT NULL, 
            password VARCHAR NOT NULL,
            type_user VARCHAR) '''
```
this query creates a table for the users, with that every user has an id, username, password and the type of user

## Products

After adding some products you can see them in a form of a table in a terminal window like this.

![Products](/screenshots/1.png) 

## bill

adding a bill is very easy all you have to to is enter the client name and the product he buys and the amount of that product and after that the class print the bill in the form of 2 tables in the terminal window like this
![bill](/screenshots/2.png)

## expences

any selling management system must have a way to enter the income and the expenses and like the bill when you enter the expenses you can see it in a form of table in the terminal window like this 
![expences](/screenshots/3.png)

## total 
after adding an expense or a bill the program calculates automatically the total expenses and the total income and the total differences and the total number of products and of course print them in a form of a table like this 
![total](/screenshots/4.png)

## save your daily report as a csv file
you can save 3 CSV files of the income and expenses and the total of any day and every day registered in the database

## save the last bill to a pdf file
you can also save the last bill to a pdf file like this 
![save the last bill to a pdf file](/screenshots/5.png)

# how to use this project

to run this project, first you need to install all the requirements using 
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
this command will print a table in the terminal window with the total revenue and total expenses and the  difference, if you want to print the hole table add 'all' to like this  "python project.py print_total_jr all"

#### `python project.py create_pdf_bill`
This command will create a pdf file and an html file for the last bill you created. 

#### ` python project.py save_to_csv `
this command will create a 3 csv file from the tables 'general bill', 'expenses', 'total'
* If you want to create a CSV file for only a specific day add the date in a format " %Y-%m-%d ". 


# Finally

Thanks for all people make CS50’s Introduction to Programming with Python possible. Especially, David J. Malan and his team for making this awesome course 

