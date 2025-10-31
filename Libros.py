import mysql.connector


class Libros:
    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="holamundo1"
        )
        return conexion

    def insertar(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "INSERT INTO libros (Title, Author, publication, Price) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def seleccionar(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "SELECT Title, Author, publication, Price FROM libros WHERE BookID=%s"
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado

    def seleccionar_todos(self):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "SELECT  BookID,Title, Author, publication, Price FROM libros"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado

    def eliminar(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "DELETE FROM libros WHERE BookID=%s"
        cursor.execute(sql, datos)
        conexion.commit()
        cant = cursor.rowcount
        conexion.close()
        return

    def Actualizar(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "UPDATE libros SET Title=%s,Author=%s, publication=%s, Price=%s WHERE BookID=%s"
        cursor.execute(sql, datos)
        conexion.commit()
        cant = cursor.rowcount
        conexion.close()
        return cant
