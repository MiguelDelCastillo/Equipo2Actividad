import sqlite3
from sqlite3 import Error
import sys

try:
    with sqlite3.connect("Soriana.db") as conn:
        cursor_registros = conn.cursor()
        
        #INSERT TABLA Vendedor
        cursor_registros.execute("INSERT INTO Vendedor VALUES(1,'Clara Itzzel', 'Montes Sánchez');")
        cursor_registros.execute("INSERT INTO Vendedor VALUES(2,'Debany Elizabeth','Ojeda Garza');")
        cursor_registros.execute("INSERT INTO Vendedor VALUES(3,'Miguel','del Castillo Vazquez');")
        
        #INSERT TABLA Cliente
        cursor_registros.execute("INSERT INTO Cliente VALUES(10,'Rolando','Ranjel Garza');")
        cursor_registros.execute("INSERT INTO Cliente VALUES(11,'Juan','Martinez Oviedo');")
        cursor_registros.execute("INSERT INTO Cliente VALUES(12,'Margarita','Estrada Saenz');")
        cursor_registros.execute("INSERT INTO Cliente VALUES(13,'Fernanda Danae','Espericueta López');")
         
        #INSERT TABLA Ventas
        cursor_registros.execute("INSERT INTO Ventas VALUES(100,'03/11/2021',1,10);")
        cursor_registros.execute("INSERT INTO Ventas VALUES(101,'03/11/2021',3,12);")
        cursor_registros.execute("INSERT INTO Ventas VALUES(102,'04/11/2021',2,11);")
        cursor_registros.execute("INSERT INTO Ventas VALUES(103,'04/11/2021',1,13);")
         
        #INSERT TABLA Detalle_venta
        cursor_registros.execute("INSERT INTO Detalle_venta VALUES('Lechuga',3,13.5,100);")
        cursor_registros.execute("INSERT INTO Detalle_venta VALUES('Kilo de plátano',1,20,100);")
        cursor_registros.execute("INSERT INTO Detalle_venta VALUES('Kilo de tomate',1,19.5,100);")
        cursor_registros.execute("INSERT INTO Detalle_venta VALUES('Kilo de fresas',1,35,101);")
        cursor_registros.execute("INSERT INTO Detalle_venta VALUES('Apio',4,5,10);")
        cursor_registros.execute("INSERT INTO Detalle_venta VALUES('Kilo de calabaza',2,15.5,102);")
        cursor_registros.execute("INSERT INTO Detalle_venta VALUES('Calabaza con casco',1,40,103);")    
        
        print("Los registros se han creado exitosamente.")
        
except Error as e:
    print(e)
except Exception:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()