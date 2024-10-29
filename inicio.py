import tkinter as tk
import requests

# Función para obtener el último registro
def obtener_ultimo_registro():
    url = "https://67212d8f98bbb4d93ca7b3de.mockapi.io/vendedoras"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            # Obtiene el último registro
            ultimo_registro = data[-1]
            return ultimo_registro
        else:
            return None
    else:
        return None

# Función para mostrar el registro en la interfaz
def mostrar_registro():
    registro = obtener_ultimo_registro()

    if registro:
        texto = f"ID: {registro['id']}\nNombre: {registro['nombre']}\nApellido: {registro['apellido']}\nCiudad: {registro['ciudad']}\nCalle: {registro['calle']}"
        etiqueta.config(text=texto)
    else:
        etiqueta.config(text="No se pudo obtener el registro.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Último Registro")

# Crear una etiqueta para mostrar el registro
etiqueta = tk.Label(ventana, text="", font=("Arial", 14), padx=10, pady=10, justify="left")
etiqueta.pack(padx=20, pady=20)

# Botón para actualizar el registro
boton_actualizar = tk.Button(ventana, text="Actualizar Registro", command=mostrar_registro)
boton_actualizar.pack(pady=10)

# Inicialmente mostrar el registro
mostrar_registro()

# Iniciar el bucle de la aplicación
ventana.mainloop()