import mysql.connector

# Función para conectar a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="129.213.62.37",
        port="3306",
        user="u1501_5d7CGSnri1",
        password="Gq2@2.ziDYg1CgkDDA8cSJMu",
        database="s1501_teczamora"
    )

# Función para ver todos los usuarios en la base de datos
def ver_usuarios():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    
    if usuarios:
        print("\nUsuarios en la base de datos:")
        for user in usuarios:
            print(f"ID: {user[0]}, Nombre: {user[1]}, Edad: {user[2]}")
    else:
        print("\nNo hay usuarios registrados.")
    
    cursor.close()
    conexion.close()

# Función para agregar un usuario
def agregar_usuario():
    nombre = input("\nIngresa el nombre de la persona: ")
    edad = input("Ingresa la edad de la persona: ")
    
    if nombre and edad.isdigit():
        conexion = conectar_db()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, int(edad)))
        conexion.commit()
        print("\nUsuario agregado correctamente.")
        cursor.close()
        conexion.close()
    else:
        print("\nError: El nombre no puede estar vacío y la edad debe ser un número válido.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Ver todos los usuarios")
        print("2. Agregar un nuevo usuario")
        print("3. Salir")
        
        opcion = input("Elige una opción (1, 2 o 3): ")
        
        if opcion == "1":
            ver_usuarios()
        elif opcion == "2":
            agregar_usuario()
        elif opcion == "3":
            print("\n¡Gracias por usar el programa! Cerrando...")
            break
        else:
            print("\nOpción no válida. Por favor elige 1, 2 o 3.")

# Ejecutar el menú
menu()
