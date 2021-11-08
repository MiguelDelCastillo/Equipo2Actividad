import sqlite3
from sqlite3 import Error
import sys

print("Bienvenido al programa!")

pregunta = input(f"\nDesea agregar una venta?: ")
if pregunta.upper() == 'SI':
    try:
        with sqlite3.connect("Soriana.db") as conn:
            conexion = conn.cursor()
            while True:
                print("A continuacion le mostraremos las claves validas")
                conexion.execute("""SELECT *\
                            FROM Cliente""")
                base_de_datos_clientes = conexion.fetchall()
                print("Id Cliente Nombre Apellidos")
                for idCliente, nombre, apellidos in base_de_datos_clientes:
                    print(idCliente, nombre, apellidos)
                id_cliente = int(input("Ingrese una clave de un cliente valida: "))
                conexion.execute("SELECT ID_cliente FROM Cliente WHERE ID_Cliente = ?", (id_cliente,))
                verificacion_id_cliente = conexion.fetchall()
                if verificacion_id_cliente:
                    break
                else:
                    print("Ingresa una clave valida")
            
            while True:
                conexion.execute("""SELECT *\
                                FROM Vendedor""")
                base_de_datos_vendedor = conexion.fetchall()
                print("Id Vendedor Nombre Apellidos")
                for idVendedor, nombre, apellidos in base_de_datos_vendedor:
                    print(idVendedor, nombre, apellidos)
                id_vendedor = int(input("Ingrese una clave de un vendedor valida: "))
                conexion.execute("SELECT ID_vendedor FROM Vendedor WHERE ID_vendedor = ?", (id_vendedor,))
                verificacion_id_vendedor = conexion.fetchall()
                if verificacion_id_vendedor:
                    print("Clave Valida!")
                    break
                else:
                    print("Ingresa una clave valida")
    except Error as e:
        print(e)
    except Exception:
        print(f"Error: {sys.exc_info()[0]}")
    finally:
        if conn:
            conn.close()
else:
    print("Tenga buen dia!")
