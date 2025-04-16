USE mydb;

CREATE TABLE users (
                       id INT AUTO_INCREMENT,
                       name VARCHAR(255) NOT NULL,
                       email VARCHAR(255) NOT NULL,
                       CONSTRAINT users_pk PRIMARY KEY (id)
);