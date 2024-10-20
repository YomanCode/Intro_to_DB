CREATE TABLE Books(
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE
);

CREATE TABLE Authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);

CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE Orders(
    order_id INT PRIMARY KEY,
    customer_id INT PRIMARY KEY,
    order_date DATE
);

CREATE TABLE Order_Details(
    order
    order_id PRIMARY KEY,
    book_id PRIMARY KEY,
    quantity DOUBLE
);