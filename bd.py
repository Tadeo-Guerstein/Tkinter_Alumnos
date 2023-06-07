import sqlite3 as bd

class BaseDeDatos:
    def abrir(self):
        conexion = bd.connect("bd_alumnos.db")
        return conexion