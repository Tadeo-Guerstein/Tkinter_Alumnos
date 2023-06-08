import sqlite3 as bd

class BaseDeDatos:
    def abrir(self):
        conexion = bd.connect("bd_alumnos.db")
        conexion.execute("create table if not exists alumnos (dni integer primary key not null, nombre text not null, apellido text not null)")
        return conexion
    
    def ingresarAlumnos(self, values):
        try:
            cone = self.abrir()
            cone.execute("insert into alumnos (dni, nombre, apellido) values (?, ?, ?)", values)
            cone.commit()
        finally:
            cone.close()

    def buscarAlumno(self, dni):
        try:
            cone = self.abrir()
            cursor = cone.execute("select dni,nombre,apellido from alumnos where dni=?", (dni, ))
            fila = cursor.fetchone()
            return fila
        finally:
            cone.close()

    def buscarAlumnos(self):
        try:
            cone = self.abrir()
            cursor = cone.execute("select dni,nombre,apellido from alumnos")
            fila = cursor.fetchall()
            return fila
        finally:
            cone.close()
    
    def modificarAlumnos(self, values):
        try:
            cone = self.abrir()
            cone.execute("update alumnos set nombre=?, apellido=? where dni=?", values)
            cone.commit()
        finally:
            cone.close()

    def borrarAlumnos(self, dni):
        try:
            cone = self.abrir()
            cone.execute("delete from alumnos where dni=?", (dni, ))
            cone.commit()
        finally:
            cone.close()