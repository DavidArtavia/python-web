import reflex as rx
import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Cambia por tu host, ejemplo: "localhost"
            user="david",  # Cambia por tu usuario de MySQL
            password="Ariasd12.",
            database="prueba",  # Cambia por tu base de datos, ejemplo: "mi_base"
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None


def insert_student(
    connection,
    nombre,
    carne,
    plan_estudios,
    herencia_martes,
    herencia_jueves,
    asignado_martes_1,
    asignado_jueves_1,
    asignado_martes_2=None,
    asignado_jueves_2=None,
    asignado_martes_3=None,
    asignado_jueves_3=None,
    casos_asignados_mes=None,
    total_casos_mes=None,
    profesora_guia=None,
):
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO estudiantes (nombre, carne, plan_estudios, herencia_martes, herencia_jueves,
                              asignado_martes_1, asignado_jueves_1, asignado_martes_2, asignado_jueves_2,
                              asignado_martes_3, asignado_jueves_3, casos_asignados_mes, total_casos_mes,
                              profesora_guia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            nombre,
            carne,
            plan_estudios,
            herencia_martes,
            herencia_jueves,
            asignado_martes_1,
            asignado_jueves_1,
            asignado_martes_2,
            asignado_jueves_2,
            asignado_martes_3,
            asignado_jueves_3,
            casos_asignados_mes,
            total_casos_mes,
            profesora_guia,
        )
        cursor.execute(query, values)
        connection.commit()
        print("Registro insertado exitosamente")
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        if cursor:
            cursor.close()
