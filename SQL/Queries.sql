SELECT num FROM paymentcards WHERE user_username = %s
SELECT num FROM paymentcards WHERE num = %s
SELECT expiry FROM paymentcards WHERE num = %s
SELECT digit_code_3 FROM paymentcards WHERE num = %s
SELECT fname FROM paymentcards WHERE num = %s
SELECT lname FROM paymentcards WHERE num = %s
SELECT address_uid FROM user_has_address WHERE user_username = %s
SELECT * FROM addresses WHERE uid = %s
SELECT uid FROM addresses WHERE uid = %s
SELECT street_num FROM addresses WHERE uid = %s
SELECT street FROM addresses WHERE uid = %s
SELECT city FROM addresses WHERE uid = %s
SELECT country FROM addresses WHERE uid = %s
SELECT postal_code FROM addresses WHERE uid = %s
SELECT address_uid FROM user_has_address WHERE user_username = %s
SELECT uid FROM addresses WHERE uid = %s
SELECT street_num FROM addresses WHERE uid = %s
SELECT street FROM addresses WHERE uid = %s
SELECT city FROM addresses WHERE uid = %s
SELECT country FROM addresses WHERE uid = %s
SELECT postal_code FROM addresses WHERE uid = %s
INSERT INTO orders(user_username, bill_num, bill_expiry, bill_digit_code_3, bill_fname, bill_lname, bill_street_num, bill_street, bill_city, bill_postal_code, bill_country, ship_street_num, ship_street, ship_city, ship_postal_code, ship_country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING num
SELECT * FROM books WHERE isbn = %s
INSERT INTO order_has_book(book_isbn, price_per_unit, quantity, order_num) VALUES (%s, %s, %s, %s)
UPDATE books SET quantity = quantity - %s WHERE isbn = %s
SELECT username, fname, lname, type, password FROM users WHERE username = %s AND password = %s
SELECT * FROM books WHERE isbn = %s
DELETE FROM books WHERE isbn = %s
INSERT INTO user_has_address (address_uid, user_username) VALUES (%s,%s)
INSERT INTO addresses (street_num, street, city, postal_code, country, type, name) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING uid
INSERT INTO users (username, fname, lname, type, password) VALUES (%s, %s, %s, %s, %s) RETURNING username
SELECT author_uid FROM author_has_book WHERE book_isbn = %s
SELECT fname, lname FROM authors WHERE uid = %s
SELECT genre FROM genres WHERE book_isbn = %s
SELECT name FROM publishers WHERE email = %s
SELECT * FROM books WHERE name = %s
SELECT uid FROM authors WHERE fname = %s AND lname = %s
SELECT book_isbn FROM author_has_book WHERE author_uid = %s
SELECT * FROM books WHERE isbn = %s
SELECT * FROM Books WHERE isbn = %s
SELECT book_isbn FROM genres WHERE genre = %s
SELECT * FROM Books WHERE isbn = %s
INSERT INTO addresses (street_num, street, city, postal_code, country, type, name) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING uid
INSERT INTO user_has_address (address_uid, user_username) VALUES (%s,%s)
INSERT INTO paymentcards (num, expiry, digit_code_3, fname, lname, user_username) VALUES (%s,%s,%s,%s,%s,%s)
    



--The %s represent the values that we inputted








