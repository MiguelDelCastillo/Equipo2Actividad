import sqlite3
from sqlite3 import Error
import sys


try:
    with sqlite3.connect("Soriana.db") as conn:
        conexion = conn.cursor()
        conexion.execute("""CREATE TABLE IF NOT EXISTS Vendedor\
                                (ID_vendedor INTEGER PRIMARY KEY,\
                                Nombre TEXT NOT NULL,\
                                Apellidos TEXT NOT NULL);\
                                """)
        conexion.execute("""CREATE TABLE Cliente \
                                (ID_cliente INTEGER NOT NULL PRIMARY KEY,\
                                Nombre TEXT NOT NULL,\
                                Apellidos TEXT NOT NULL);\
                                """)
        conexion.execute("""CREATE TABLE Ventas\
                                (Folio INTEGER PRIMARY KEY,\
                                  fecha TEXT NOT NULL,\
                                  ID_vendedor INTEGER NOT NULL,\
                                  ID_cliente INTEGER NOT NULL,\
                                  FOREIGN KEY (ID_vendedor) REFERENCES Vendedor(ID_vendedor), \
                                  FOREIGN KEY (ID_cliente) REFERENCES Cliente(ID_cliente) \
                                );""")
        conexion.execute("""CREATE TABLE Detalle_venta \
                            (Descripcion TEXT NOT NULL,\
                              Cant_pzs INTEGER NOT NULL,\
                              Precio_unitario FLOAT NOT NULL,\
                              Folio INTEGER NOT NULL,\
                              FOREIGN KEY (Folio) REFERENCES Ventas(Folio)\
                            );""")
except Error as e:
    print(e)
except Exception:
    print(f"Error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()