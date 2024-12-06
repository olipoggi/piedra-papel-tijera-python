#tarea: 
#que lo ingresado sea lowercase de tal forma de comparar minuscula y mayuscyka
# #agregar mas de un turno con el bucle while 

nombre1 = input("¿Cómo te llamas jugador 1?: ")
nombre2 = input("¿Cómo te llamas jugador 2?: ")

# Variables para contar victorias
victorias1 = 0
victorias2 = 0
rondas = 0  # Contador de rondas

# Bucle principal para jugar hasta 5 rondas o que alguien gane 3 veces
while rondas < 5 and victorias1 < 3 and victorias2 < 3:
    print(f"\nRonda {rondas + 1} de 5")
    jugador1 = input(f"¡Hola {nombre1}! ¿Qué elegís? piedra, papel o tijera: ").lower()
    jugador2 = input(f"¡Hola {nombre2}! ¿Qué elegís? piedra, papel o tijera: ").lower()

    # Condiciones para determinar el ganador de la ronda
    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("Empate en esta ronda.")
    elif condicion1 or condicion2 or condicion3:
        print(f"Gana esta ronda {nombre1}!")
        victorias1 += 1
    else:
        print(f"Gana esta ronda {nombre2}!")
        victorias2 += 1

    rondas += 1  # Incrementar el contador de rondas

# Determinar el ganador final
if victorias1 > victorias2:
    print(f"\n¡{nombre1} gana el mejor de 3 con {victorias1} victorias!")
elif victorias2 > victorias1:
    print(f"\n¡{nombre2} gana el mejor de 3 con {victorias2} victorias!")
else:
    print("\nEmpate en el mejor de 3.")

