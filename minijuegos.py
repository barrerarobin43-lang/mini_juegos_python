import random
print("Bienvenido al juego adivina el numero")
numero_secreto = random.randint(1, 50)
adivinado = False
while not adivinado:
    intento = int(input("dame un numero de entre 1 y 50: "))
    if intento < numero_secreto:
        print("valor demasiado bajo: ")
    elif intento > numero_secreto:
        print("valor demasiado alto: ")
    else:
        print("acertaste, wiii")
        adivinado = True
        input("Presiona Enter para salir...")