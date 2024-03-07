-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS portfolio_final_db;
CREATE USER IF NOT EXISTS 'portfolio_final'@'localhost' IDENTIFIED BY 'portfolio_final_pwd';
GRANT ALL PRIVILEGES ON `portfolio_final_db`.* TO 'portfolio_final'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'portfolio_final'@'localhost';
FLUSH PRIVILEGES;
