CREATE DATABASE comercio;

USE comercio;

CREATE TABLE usuarios (
		ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        usuario varchar(50) NOT NULL,
        senha varchar(50) NOT NULL,
        tipo_user varchar(50) NOT NULL
);

DROP TABLE usuarios;

SELECT * FROM usuarios;

FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON * . * TO 'user_test'@'localhost'; 

CREATE USER 'user_test'@'localhost' IDENTIFIED BY '123';

SHOW GRANTS FOR 'user_test'@'localhost';
GRANT CREATE USER ON *.* TO 'root'@'localhost';
DELETE FROM usuarios WHERE ID > 3;
