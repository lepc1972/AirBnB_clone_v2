-- configuration database for AirBnB project

-- creates database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creates a database user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

-- creates user password
SET PASSWORD FOR 'hbnb_dev'@'localhost' = PASSWORD('hbnb_dev_pwd');

-- add privileges to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
