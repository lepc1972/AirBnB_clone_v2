-- configuration database for AirBnB project

-- creates database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creates a database user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- creates user password
SET PASSWORD FOR 'hbnb_test'@'localhost' = PASSWORD('hbnb_test_pwd');

-- add privileges to the user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
