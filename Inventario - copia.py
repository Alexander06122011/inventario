import sqlite3
from datetime import datetime

# --- CONFIGURACIÓN DE LA BASE DE DATOS ---
conn = sqlite3.connect("precios.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    precio REAL,
    fecha TEXT
)
""")
conn.commit()

# --- FUNCIÓN PARA GUARDAR LOS DATOS ---
def guardar_producto(nombre, precio):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO productos (nombre, precio, fecha) VALUES (?, ?, ?)",
                   (nombre, precio, fecha))
    conn.commit()
    print(f"Producto '{nombre}' guardado con precio {precio} en {fecha}\n")

# --- SISTEMA PRINCIPAL ---
def sistema():
    while True:
        try: 
            nombre = input("Ingresa el nombre del producto (o 'salir' para terminar):\n")
            if nombre.lower() == "salir":
                print("Gracias por usar nuestro sistema.\n")
                break

            cantidad = input("Ingresa la cantidad de productos:\n")
            if cantidad.lower() == "salir":
                print("Gracias por usar nuestro sistema.\n")
                break
            else:
                cantidad = int(cantidad)
            
            precio = input("Ingresa el precio por producto:\n")
            if precio.lower() == "salir":
                print("Gracias por usar nuestro sistema.\n")
                break
            else:
                precio = float(precio)
            
            total = cantidad * precio
            print(f"El valor total es: {total}\n")

            # Guardar en base de datos
            guardar_producto(nombre, precio)

        except ValueError:
            print("Solo se pueden ingresar números en cantidad y precio.\n")
        except KeyboardInterrupt:
            print("\nGracias por usar nuestro sistema.\n")
            break

# --- PUNTO DE ENTRADA ---
def main():
    sistema()
    conn.close()

if __name__ == "__main__":
    main()
