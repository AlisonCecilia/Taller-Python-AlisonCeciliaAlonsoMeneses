import mariadb
from setuptools.command.egg_info import manifest_maker


def conectar_y_comsultar():
    try:
        #Establecer conexion ala base de datos
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306
        )
        print(f"Tipo de conexion {type(conexion)}")
        print("Conexión a la Base de Datos del servidor Ounus")

        #Crear un cursor y ejecutar la consulta
        cursor=conexion.cursor()
        consulta= "select * from usuarios"
        cursor.execute(consulta)

        #Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("resultado ", type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:
            print(f"ID: {fila[0]},nombre_completo: {fila[1]} Nombre de Usuario: {fila[2]}, Correo: {fila[3]}, contraseña: {fila[4]}, Id_Rol: {fila[5]}")

    except mariadb.Error as e:
        print(f"Error al conectar con la base dedatos: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("onexion cerRADA.")

if __name__ == '__main__':
    conectar_y_comsultar()