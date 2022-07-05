# selling management system
#### Video Demo:  <URL HERE>
#### Description:

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
this command will print a table in the terminal window with the total revenue and total expenses and the  difference, if you want to print a total table for a specific date, add the day in a format "%Y-%m-%d" after "python project.py print_total_jr"

#### `python project.py create_pdf_bill`
This command will create a pdf file and an html file for the last bill you created. 

#### ` python project.py save_to_csv `
this command will create a 3 csv file from the tables 'general bill', 'expenses', 'total'
* If you want to create a CSV file for only a specific day add the date in a format " %Y-%m-%d ". 