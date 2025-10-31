import mysql.connector


class Empleados:
    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db3"
        )
        return conexion

    def alta(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "INSERT INTO empleados (nombre, cargo) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def consulta(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "SELECT nombre, cargo FROM empleados WHERE id_empleado=%s"
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado

    def recuperar_todos(self):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "SELECT id_empleado, nombre, cargo FROM empleados"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado

    def baja(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "DELETE FROM empleados WHERE id_empleado=%s"
        cursor.execute(sql, datos)
        conexion.commit()
        cant = cursor.rowcount
        conexion.close()
        return

    def modificacion(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "UPDATE empleados SET nombre=%s, cargo=%s WHERE id_empleado=%s"
        cursor.execute(sql, datos)
        conexion.commit()
        cant = cursor.rowcount
        conexion.close()
        return cant



