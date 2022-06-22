CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    type TEXT,
    descreption TEXT,
    montant REAL,
    date TEXT,
    time TEXT
);


CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    product_name TEXT,
    prix REAL,
    royltie REAL,
    product_descreption TEXT
);


CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    username TEXT UNIQUE,
    password TEXT,
    type_user TEXT
);


CREATE TABLE general_bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    client_name TEXT,
    total REAL,
    number_of_products INTEGER,
    date TEXT,
    time TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users`(id`)
);


CREATE TABLE details_bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    products INTEGER,
    number_of_products INTEGER,
    prix REAL,
    royltie REAL,
    date TEXT,
    time TEXT,
    general_bill_id INTEGER,
    FOREIGN KEY (general_bill_id) REFERENCES general_bill`(id`),
    FOREIGN KEY (products) REFERENCES product`(id`)
);