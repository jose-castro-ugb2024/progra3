import mysql.connector

conexion1= mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="",
                                   database="db2")

cursor1 = conexion1.cursor()
print("\n=== LISTA ACTUALIZADA ===")
cursor1.execute("SELECT id, descripcion, precio FROM articulos")
for datos in cursor1:
    print(datos)
conexion1.close()
print("Listo...")



