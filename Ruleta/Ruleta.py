'''
Descripción: Nos encontramos en un juego de apuestas muy conocido como ruleta, en donde
reeborg girara de manera aleatoria alrededor del mapa y el usuario debe escoger en donde en donde cree que va a caer
en dicho caso que acierte ganara, dependiendo del objeto que haya escogido, en caso contrario el usuario
perdera lo apostado.
Autores:brayan Alejandro cruz-Tomas arango niño
'''
# Importa la libreria random
import random
# Activar el sonido
sound(True)

coins = 1
ganador1 = ""
'''
Descripción: Valida si en la casilla hay algún objeto.
Hace la acción indicada para cada objeto.
'''    
def recolectar():
    global coins
    global ganador1
    if object_here("tulip"):
        if ganador1 == "tulipan":
            coins *= 30
            print("Felicidades ganaste",coins,"coins")
        else:
            print("Lo siento perdiste, cayó tulipan")
            print("Tu seleccionaste",ganador1)
    elif object_here("triangle"):
        if ganador1 == "triangulo":
            coins *= 400
            print("Felicidades ganaste",coins,"coins")
        else:
            print("Lo siento perdiste, cayó triangulo")
            print("Tu seleccionaste",ganador1)
    elif object_here("star"):
        if ganador1 == "estrella":
            coins *= 10
            print("Felicidades ganaste",coins,"coins")
            print("Tu seleccionaste",ganador1)
        else:
            print("Lo siento perdiste, cayó estrella")
    elif object_here("token"):
        if ganador1 == "carita":
            coins *= 5000
            print("Felicidades ganaste",coins,"coins")
        else:
            print("Lo siento perdiste, cayó carita")
            print("Tu seleccionaste",ganador1)
'''
Descripción: Esta función hace girar a Reeborg las veces que el random haya seleccionado
'''
def mover(dado):
    think(1)
    global ganador1
    seleccion = input("Coins iniciales = 1;       La estrella multiplica x 10;             El triangulo multiplica x 400;              El tulipan multiplica x 30;                     La carita multiplica x 5000;                        Selecciona la figura que crees que va a caer: estrella, triangulo, tulipan o carita y dale aceptar para empezar")
    ganador1 = seleccion
    # Se mueve mientras hayan movimientos
    while dado != 0:
        move()
        if wall_in_front():
            turn_left()
        dado -= 1
    recolectar()

x = random.randrange(50, 100)
mover(x)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
