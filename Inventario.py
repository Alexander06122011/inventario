def sistema():
    while True:
        try: 
            cantidad = int(input("Ingresa la cantidad de productos:\n"))
            precio = int(input("Ingresa el precio por prducto:\n"))
            print(f"El valor total es: {cantidad * precio}")
            break
        except ValueError:
            print("Solo se pueden ingresar números")
        except KeyboardInterrupt:
            print("Gracias por usar nuestro sistema\n")
            break
            
        
sistema()
