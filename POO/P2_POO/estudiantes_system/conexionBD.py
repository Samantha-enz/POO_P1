import mysql.connector

try:
    conexion=mysql.connector.connect(
        host= "127.0.0.1",
        user = 'root',
        password='',
        database='bd_estudiantes'

    )
    cursor=conexion.cursor(buffered=True)

except:
    print("\t\t\t..... ¡Por el momento no es posible conectar con la base de datos, intente más tarde! .....")