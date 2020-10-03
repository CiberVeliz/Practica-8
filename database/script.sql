CREATE DATABASE SA;

USE SA;

CREATE TABLE Estudiante
(
    carne INT NOT NULL,
    nombre VARCHAR(32) NOT NULL,
    apellido VARCHAR(32) NOT NULL
);


INSERT INTO Estudiante(carne, nombre, apellido) VALUES
(201602959, 'Jose Manuel', 'Veliz Sandoval'),
(201602988, 'Ozmar Rene', 'Escobar Avila'),
(201603191, 'Pablo Andres', 'Hernandez Rivera');