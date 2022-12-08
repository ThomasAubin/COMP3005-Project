-- Import UUID module
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


-- Remove any pervious tables
DROP TABLE IF EXISTS users, user_has_paymentcard, paymentcards, user_has_order, orders, user_has_address CASCADE;




-- -----------------------
-- Create tables
-- -----------------------

CREATE TABLE users
    (uid uuid DEFAULT uuid_generate_v4(), 
     fname VARCHAR(15),
     lname VARCHAR(15),

     PRIMARY KEY (uid)
    );

CREATE TABLE user_has_paymentcard
    (paymentcard_num CHAR(16),
     user_uid uuid,

     PRIMARY KEY (paymentcard_num)
    );

CREATE TABLE paymentcards
    (num CHAR(16),
     expiry CHAR(4) NOT NULL,
     digitcode3 INT NOT NULL,
     fname VARCHAR(15),
     lname VARCHAR(15),

     PRIMARY KEY (num)
    );

CREATE TABLE user_has_order
    (order_num uuid,
     user_uid uuid,

     PRIMARY KEY (order_num)
    );

CREATE TABLE orders
    (order_num uuid DEFAULT uuid_generate_v4(),
     date_ordered DATE,
     tracking_num uuid DEFAULT uuid_generate_v4(),

     payment_num CHAR(16),
     payment_expiry CHAR(4) NOT NULL,
     payment_3digitcode INT NOT NULL,
     payment_fname VARCHAR(15),
     payment_lname VARCHAR(15),

    -- Addpayment address

    -- Add shipping address

     PRIMARY KEY (order_num)
    );

CREATE TABLE user_has_address 
    (address_uid uuid,
     user_uid uuid,

     PRIMARY KEY (address_uid)
    );




-- -----------------------
-- Create relationships
-- -----------------------
