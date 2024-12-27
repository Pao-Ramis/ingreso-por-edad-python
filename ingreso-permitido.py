# Paso 1: Solicitar al usuario que ingrese la edad

edad = int(input("Por favor, ingresa tu edad "))


#Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar

permitido = True if edad >= 18 else False #ternario


# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca

if permitido:
    print("El cliente puede ingresar a la discoteca")
else:
    print("Lo sentimos, el cliente no puede ingresar a la discoteca siendo menor de edad")