import tkinter as tk
from tkinter import messagebox
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="TuHost",
        port="3306",
        user="UserName",
        password="Password",
        database="database"
    )

def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS register (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()

def registrar_usuario():
    username = entry_user.get()
    password = entry_pass.get()
    
    if username and password:
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            sql = "INSERT INTO register (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
            conexion.commit()
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "El usuario ya existe")
        finally:
            cursor.close()
            conexion.close()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

def login_usuario():
    username = entry_user.get()
    password = entry_pass.get()
    
    conexion = conectar_db()
    cursor = conexion.cursor()
    sql = "SELECT * FROM register WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    conexion.close()
    
    if user:
        messagebox.showinfo("Bienvenido", f"Hola {username}!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear tabla si no existe
crear_tabla()

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Login & Register")
root.geometry("500x500")
root.configure(bg="#1E1E1E")

frame = tk.Frame(root, bg="#2C2F33", padx=40, pady=40, bd=5, relief="ridge")
frame.pack(pady=50)

title_label = tk.Label(frame, text="🔐 Bienvenido", fg="#FFFFFF", bg="#2C2F33", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

tk.Label(frame, text="Usuario:", fg="white", bg="#2C2F33", font=("Arial", 12)).pack()
entry_user = tk.Entry(frame, font=("Arial", 12))
entry_user.pack(pady=5)

tk.Label(frame, text="Contraseña:", fg="white", bg="#2C2F33", font=("Arial", 12)).pack()
entry_pass = tk.Entry(frame, show="*", font=("Arial", 12))
entry_pass.pack(pady=5)

button_frame = tk.Frame(frame, bg="#2C2F33")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Registrarse", command=registrar_usuario, bg="#007BFF", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Iniciar Sesión", command=login_usuario, bg="#28A745", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=5)

root.mainloop()
