-- This is a script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server
-- id INT unique, auto generated, cant be null and is a primary key
-- name VARCHAR(256) cant be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(256) NOT NULL);
