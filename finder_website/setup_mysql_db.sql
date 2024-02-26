-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS portfolio_db;
CREATE USER IF NOT EXISTS 'portfolio_db'@'localhost' IDENTIFIED BY 'portfolio_pwd';
GRANT ALL PRIVILEGES ON `portfolio_db`.* TO 'portfolio_db'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'portfolio_db'@'localhost';
FLUSH PRIVILEGES;
