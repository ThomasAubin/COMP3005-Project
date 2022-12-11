-- Import UUID module
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


-- Remove any pervious tables
DROP TABLE IF EXISTS users, paymentcards, orders, addresses, user_has_address, publishers, phone_nums, books, genres, authors, author_has_book, order_has_book CASCADE;




-- -----------------------
-- Create tables
-- -----------------------

CREATE TABLE users
    (username VARCHAR(15), 
     fname VARCHAR(15),
     lname VARCHAR(15),
     type VARCHAR(8), -- customer or manager
     password VARCHAR(15),

     PRIMARY KEY (username)
    );

CREATE TABLE paymentcards
    (num CHAR(16),
     expiry CHAR(4),
     digitcode3 INT,
     fname VARCHAR(15),
     lname VARCHAR(15),
     user_username VARCHAR(15),

     PRIMARY KEY (num),
     FOREIGN KEY (user_username) REFERENCES users(username)
    );

CREATE TABLE orders
    (num UUID DEFAULT uuid_generate_v4(),
     date_ordered DATE DEFAULT NOW(),
     tracking_num UUID DEFAULT uuid_generate_v4(),

     user_username VARCHAR(15),

     bill_num CHAR(16),
     bill_expiry CHAR(4),
     bill_digit_code_3 INT,
     bill_fname VARCHAR(15),
     bill_lname VARCHAR(15),

     bill_street_num VARCHAR(10),
     bill_street VARCHAR(25),
     bill_city VARCHAR(20),
     bill_postal_code CHAR(6),
     bill_country VARCHAR(20),

     ship_street_num VARCHAR(10),
     ship_street VARCHAR(25),
     ship_city VARCHAR(20),
     ship_postal_code CHAR(6),
     ship_country VARCHAR(20),

     PRIMARY KEY (num),
     FOREIGN KEY (user_username) REFERENCES users(username)
    );

CREATE TABLE addresses 
    (uid UUID DEFAULT uuid_generate_v4(),
     street_num VARCHAR(10),
     street VARCHAR(25),
     city VARCHAR(20),
     postal_code CHAR(6), -- Assume only Canada postal codes
     country VARCHAR(20),
     type CHAR(4), -- bill or ship
     name VARCHAR(15),

     PRIMARY KEY (uid)
    );

CREATE TABLE user_has_address 
    (address_uid UUID,
     user_username VARCHAR(15),

     PRIMARY KEY (address_uid, user_username),
     FOREIGN KEY (address_uid) REFERENCES addresses(uid),
     FOREIGN KEY (user_username) REFERENCES users(username)
    );

CREATE TABLE publishers
    (email VARCHAR(25),
     name VARCHAR(20),
     bank_num INT,
     address_uid UUID,

     PRIMARY KEY (email),
     FOREIGN KEY (address_uid) REFERENCES addresses(uid)
    );

CREATE TABLE phone_nums
    (publisher_email VARCHAR(25),
     phone_number VARCHAR(10), -- Assume 10 digit format only. XXX-XXX-XXXX

     PRIMARY KEY (publisher_email, phone_number),
     FOREIGN KEY (publisher_email) REFERENCES publishers(email)
    );

CREATE TABLE books 
    (isbn CHAR(13),
     name VARCHAR(25),
     pages INT,
     price INT,
     quantity INT,
     publisher_share_percentage INT, -- 0 to 100
     publisher_email VARCHAR(25),

     PRIMARY KEY (isbn),
     FOREIGN KEY (publisher_email) REFERENCES publishers(email)
    );

CREATE TABLE genres 
    (book_isbn CHAR(13),
     genre VARCHAR(15),

     PRIMARY KEY (book_isbn, genre),
     FOREIGN KEY (book_isbn) REFERENCES books(isbn)
    );

CREATE TABLE authors 
    (uid UUID DEFAULT uuid_generate_v4(),
     fname VARCHAR(15),
     lname VARCHAR(15),

     PRIMARY KEY (uid)
    );

CREATE TABLE author_has_book 
    (author_uid UUID,
     book_isbn CHAR(13),

     PRIMARY KEY (author_uid, book_isbn),
     FOREIGN KEY (author_uid) REFERENCES authors(uid),
     FOREIGN KEY (book_isbn) REFERENCES books(isbn)
    );

CREATE TABLE order_has_book 
    (book_isbn CHAR(13),
     price_per_unit INT,
     quantity INT,
     order_num UUID,

     PRIMARY KEY (book_isbn, order_num),
     FOREIGN KEY (book_isbn) REFERENCES books(isbn),
     FOREIGN KEY (order_num) REFERENCES orders(num)
    );
