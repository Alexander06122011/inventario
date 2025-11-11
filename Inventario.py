def sistema():
    while True:
        try: 
            cantidad = input("Ingresa la cantidad de productos:\n")
            
            if cantidad.lower() == "salir":
                print("Gracias por usar nuestro sistema\n")
                break
            else:
                cantidad = int(cantidad)
            
            precio = input("Ingresa el precio por producto:\n")
            
            if precio.lower() == "salir":
                print("Gracias por usar nuestro sistema\n")
                break
            else:
                precio = int(precio)
            print(f"El valor total es: {cantidad * precio}")
            break
        except ValueError:
            print("Solo se pueden ingresar números")
        except KeyboardInterrupt:
            print("Gracias por usar nuestro sistema\n")
            break
            
def main():
    sistema()

if __name__ == "__main__":
    main()