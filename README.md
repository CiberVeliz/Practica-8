# Practica-8
## José Manuel Véliz Sandoval - 201602959
Esta rama contiene la todo el contenido de la práctica #8, la cual consiste en utilizar docker-compose para comunicar un servicio web y una base de datos.

## Versiones de herramientas utilizadas
- Docker: 19.03.6, build 369ce74a3c
- Docker-compose: 1.21.2, build a133471

## Ejecución del .yaml
Para crear las imagenes y levantar los servicios solo es necesario correr el siguiente comando:
```
sudo docker-compose up -d
```
o
```
sudo docker-compose up
```
Y para tener la ejecución, ya se Ctrl + C o el siguiente comando:
```
sudo docker-compose down
```
Si en ninguno de los pasos anteriores ocurrió un error, se debería de visualizar la información de la base de datos en http://localhost/.

## Video
[Explicación](https://drive.google.com/file/d/1YLmgclPGUdNdPV9wLTQVP4huyFgoQQq2/view?usp=sharing)