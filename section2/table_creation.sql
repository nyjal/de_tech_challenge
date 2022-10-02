
CREATE TABLE salesperson(
salesperson_id VARCHAR(20) NOT NULL,
salesperson_name VARCHAR(100) NOT NULL,
CONSTRAINT SALESPERSON_PK PRIMARY KEY(salesperson_id)
);

CREATE TABLE customers(
customer_id VARCHAR(20) NOT NULL,
customer_name VARCHAR(100) NOT NULL,
customer_phone VARCHAR(100) NOT NULL,
CONSTRAINT CUSTOMERS_PK PRIMARY KEY(customer_id)
);

CREATE TABLE car(
serial_number VARCHAR(20),
manufacturer VARCHAR(100) NOT NULL,
model_name VARCHAR(100) NOT NULL,
weight VARCHAR(100) NOT NULL,
price DECIMAL NOT NULL,
CONSTRAINT CAR_PK PRIMARY KEY(serial_number)
);


create table transaction (
salesperson_id VARCHAR(20) NOT NULL,
customer_id VARCHAR(20) NOT NULL,
customer_phone VARCHAR(100) NOT NULL,
serial_number VARCHAR(20) NOT NULL,
manufacturer VARCHAR(100) NOT NULL,
model_name VARCHAR(100) NOT NULL,
weight VARCHAR(100) NOT NULL,
price DECIMAL NOT NULL,
txn_date DATE NOT NULL,
CONSTRAINT TRANSACTION_PK PRIMARY KEY (salesperson_id, customer_id, serial_number),
CONSTRAINT TRANSACTION_PK1 FOREIGN KEY (salesperson_id) references salesperson (salesperson_id),
CONSTRAINT TRANSACTION_PK2 FOREIGN KEY (customer_id) references customers (customer_id),
CONSTRAINT TRANSACTION_PK3 FOREIGN KEY (serial_number) references car (serial_number)
);


