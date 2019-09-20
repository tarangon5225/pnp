'''
Nos encontramos con un juego denominado escalera, en un mundo de 12x12.
donde se enfrentarán 2 robots atravesando todo el mundo
encontrarán ayudas o trampas para llegar a la meta
LAS REGLAS SON:
1) Será considerado ganador, el primer jugador en llegar a la meta, casilla (1,12).
2) Solo será un turno de movimiento y posteriormente pasará el turno, el siguiente jugador hará lo mismo.
AYUDAS:
- BEEPER: Si Reeborg se detiene sobre un Beeper,
automáticamente este será impulsado una fila.
- ESTRELLA: Si Reeborg se detiene sobre una estrella,
avanza de nuevo la cantidad de casillas que obtuvo en el dado.
TRAMPAS:
- TULIPAN: Si Reeborg se detiene sobre un tulipán, da un giro de 180°
y se regresará las casillas avanzadas.
- TRIANGULO: Si Reeborg se detiene sobre de un triángulo, este hará que baje una linea.
Autores: Brayan Cruz - Tomás Arango
Fecha de entrega:20/09/2019
'''
# Aumenta la cantidad de pasos que puede ejecutar Reeborg a 10000
#think(1)
set_max_nb_steps(10000)
#Activar el sonido
sound(True)
# Importa la libreria random
import random
'''
Descripción: Esta función se usa con el fin de utilizar los robots
que sean necesarios, dependiendo a la cantidad de reeborgs que vamos a usar, se puede como máximo 4 jugadores
'''
r1 = UsedRobot()
r2 = UsedRobot()

#Variables globales
mover = 0
mover_1 = 0
robot = r1
turn = 0
player_1 = ""
player_2 = ""

'''
Descripción: Reeborg gira a la derecha
Pos: Reeborg gira 270° de la posición inicial
'''
def turn_right():
    repeat 3:
        robot.turn_left()
'''
Descripción: Caminar hacia el frente mientras no encuentre pared.
Antes de avanzar valida si hay elementos y lo recoge.
Pre: Reeborg mira hacia la derecha || mira hacia la izquierda
Pos: Reeborg avanzó hasta donde encontró pared &&
mira hacia la derecha || mira hacia la izquierda
'''
def walk():
    global mover
    # Mientras hayan movimientos restantes avanza
    while mover != 0:
        if robot.front_is_clear():
            robot.move()
            mover -= 1
        else:
            break
    if mover == 0:
        recolectar()
            
'''
Descripción: Cambia de fila en el limite derecho del mundo.
Antes de avanzar valida si hay elementos y lo recoge.
Pre: Reeborg está en el X mayor && mira hacia la derecha
Pos: Reeborg está en el X mayor && y+=1 && mira hacia la izquierda
'''
def change_lineR():
    global mover
    if mover != 0:
        robot.turn_left()
        robot.move()
        mover -= 1
        robot.turn_left()
    else:
        recolectar()
'''
Descripción: Cambia de fila en el limite izquierdo del mundo.
Antes de avanzar valida si hay elementos y lo recoge.
Pre: Reeborg está en x=1 && mira hacia la izquierda
Pos: Reeborg está en x=1 && y+=1 && mira hacia la derecha
'''
def change_lineL():
    global mover
    if mover != 0:
        turn_right()
        robot.move()
        mover -= 1
        turn_right()
    else:
        recolectar()
'''
Descripción: Reeborg avanza por el mundo, en zigzag.
Recibe un número entero X, donde 1<=X<=6
Pre: Reeborg debe estar en un mundo de 12*12, en la casilla (1,1)
Mirando hacia la derecha.
Pos: Reeborg está en la casilla (12,1) mirando hacia la izquierda.
'''    
def walk_world(dado):
    global mover
    global mover_1
    global turn
    global player_1
    global player_2
    mover = dado
    mover_1 = dado
    walk()
    en_meta()
    if robot.object_here("square"):
        change_lineR()
        walk()
    elif robot.object_here("token"):
        robot.take("token")
        if turn == 1:
            print("Ganaste ",player_1,"¡Felicitaciones!")
            print("Tu Robot fue el ganador")
        else:
            print("Ganaste ",player_2,"¡Felicitaciones!")
            print("Tu Robot fue el ganador")
        done()
    else:
        change_lineL()
        walk()

'''
Descripción: Valida si en la casilla hay algún objeto y lo recoge.
Hace la acción indicada para cada objeto.
'''    
def recolectar():
    global mover_1
    if robot.object_here("tulip"):
        robot.turn_left()
        robot.turn_left()
        # Contar los pasos que avanzó y se devuelve
        while mover_1 != 0:
            robot.move()
            mover_1 -= 1
        robot.turn_left()
        robot.turn_left()
    elif robot.object_here("triangle"):
        robot.turn_left()
        robot.move()
        robot.turn_left()
    elif robot.object_here("beeper"):
        robot.turn_left()
        robot.move()
        robot.turn_left()
    elif robot.object_here("star"):
        # Avanza el doble de lo que lanzó en el dado
        while mover_1 != 0:
            robot.move()
            mover_1 -= 1

'''
Descripción: Permite el movimiento de los robots
Recibe el número de casillas que avanza donde 0 < avanza < 7
Recibe el jugador que tiene el turno donde 0 < jugador < 3
'''
def turno(avanza, jugador):
    #think(1)
    global robot
    global turn
    turn = jugador
    if jugador == 1:
        robot = r1
        walk_world(avanza)
    elif jugador == 2:
        robot = r2
        walk_world(avanza)
'''
Descripción: Valida que Reeborg se encuentre en la esquina superior izquierda del mundo.
Retorna True si se encuentra en la meta || retorna False si no está en la meta.
'''
def en_meta():
    global turn
    if wall_in_front():
        if wall_on_right():
            return True
    else:
        return False

'''
Descripción: Función que permite ingresar los nombres de los jugadores, imprime las reglas del juego
y mientras Reeborg no haya llegado a la meta, cada jugador lanze el dado.
'''
def jugar():
    global player_1
    global player_2
    player1 = input("Escriba el nombre del jugador 1: ")
    player_1 = player1
    player2 = input("Escriba el nombre del jugador 2: ")
    player_2 = player2
    print("Nos encontramos con un juego denominado escalera, en un mundo de 12x12.")
    print("donde se enfrentarán 2 robots atravesando todo el mundo")
    print("encontrarán ayudas o trampas para llegar a la meta")
    print("LAS REGLAS SON:")
    print("1) Será considerado ganador, el primer jugador en llegar a la meta, casilla (1,12).")
    print("2) Solo será un turno de movimiento y luego pasará el turno, el siguiente jugador hará lo mismo.")
    print("AYUDAS:")
    print("- BEEPER: Si Reeborg se detiene sobre un Beeper,")
    print("automáticamente este será impulsado una fila.")
    print("- ESTRELLA: Si Reeborg se detiene sobre una estrella,")
    print("avanza de nuevo la cantidad de casillas que obtuvo en el dado.")
    print("TRAMPAS:")
    print("- TULIPAN: Si Reeborg se detiene sobre un tulipán, da un giro de 180°")
    print("y se regresará las casillas avanzadas.")
    print("- TRIANGULO: Si Reeborg se detiene sobre de un triángulo, este hará que baje una linea.")
    pause()
    # Mientras Reeborg no está en la meta, se juega por turnos
    while not en_meta():
        print("Es turno de: ",player1)
        uno = input("Escriba 1 para lanzar el dado: ")
        if uno == "1":
            x1 = random.choice((1,2,3,4,5,6))
            print(player1," sacó ", x1)
            turno(x1,1)
        print("Es turno de: ",player2)
        dos = input("Escriba 2 para lanzar el dado: ")
        if dos == "2":
            x2 = random.choice((1,2,3,4,5,6))
            print(player2," sacó ", x2)
            turno(x2,2)
    
jugar()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
