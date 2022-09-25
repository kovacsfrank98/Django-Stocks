CREATE DATABASE django_stocks;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'Bri@nna08';
GRANT ALL PRIVILEGES ON `django_stocks` . * TO 'root'@'localhost';
FLUSH PRIVILEGES;