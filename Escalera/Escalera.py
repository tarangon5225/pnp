'''
Descripción: Nos encontramos con un juego muy conocido por todos denominado escalerita en un mundo de 12*12, donde se enfrentarán
los jugadores atravesando por todo el mundo encontraran ayudas o dificultades para llegar a la meta, avanzaran de manera
escalonada por filas, hasta llegar a su meta.
LAS REGLAS SON:
1) Será considerado ganador, el primer jugador en llegar a la meta casilla (1,12).
2) Para iniciar se lanzará un dado, quien saque el mayor número iniciará la partida.
3) Solo será un turno de movimiento y posteriormente pasará el turno, el siguiente jugador hará lo mismo.
4) El jugador que robe turno, será penalizado perdiendo su siguiente turno.
AYUDAS Y TRAMPAS:
- BEEPER: Si reeborg se detiene sobre un Beeper, automáticamente este será impulsado por su fuerza y podrá subir una fila.
- ESTRELLA: Si Reeborg se detiene sobre una estrella, avanza de nuevo la cantidad de casillas que obtuvo en el dado.
- TULIPAN: Cuando Reeborg se detiene sobre un tulipán él lo come generando una confusión de donde se encuentra, da un giro de
    180° y se regresará las casillas avanzadas.
- TRIANGULO: Si Reeborg para encima de un trangulo, este afectara sus sentidos y hara que baje una linea.
Autores: Brayan Cruz - Tomás Arango
Fecha de entrega:18/09/2019
'''
'''
Descripción: Esta función se usa con el fin de utilizar los robots
que sean necesarios, dependiendo a la cantidad de reeborgs que vamos a usar, se puede como máximo 4 jugadores
'''

r1 = UsedRobot()
r2 = UsedRobot()
r3 = UsedRobot()
r4 = UsedRobot()

#Variables globales
mover = 0
mover_1 = 0

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
    while mover != 0:
        if front_is_clear():
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
        robot.turn_right()
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
    think(1)
    global mover
    global mover_1
    mover = dado
    mover_1 = dado
    robot.walk()
    if object_here("square"):
        change_lineR()
        walk()
    else:
        change_lineL()
        walk()

'''
Descripción: Valida si en la casilla hay algún objeto y lo recoge.
Hace la acción indicada para cada objeto.
'''    
def recolectar():
    global mover_1
    if object_here("tulip"):
        robot.take("tulip")
        robot.turn_left()
        robot.turn_left()
        while mover_1 != 0:
            robot.move()
            mover_1 -= 1
        robot.turn_left()
        robot.turn_left()
    elif object_here("triangle"):
        robot.take("triangle")
        robot.turn_left()
        robot.move()
        robot.turn_left()
    elif object_here("beeper"):
        robot.take("beeper")
        robot.turn_left()
        robot.move()
        robot.turn_left()
    elif object_here("star"):
        robot.take("star")
        while mover_1 != 0:
            robot.move()
            mover_1 -= 1
        
#walk_world(5)
#walk_world(6)

'''
Descripción: Permite el movimiento del Reeborg escogido para cada jugador.
Recibe el número de casillas que avanza donde 0 < avanza < 7
Recibe el jugador que tiene el turno donde 0 < jugador < 5
'''
def turno(avanza, jugador):
	if jugador == 1:
		robot = r1
		walk_world(avanza)
	elif jugador == 2:
		robot = r2
		walk_world(avanza)
	elif jugador == 3:
		robot = r3
		walk_world(avanza)
	elif jugador == 4:
		robot = r4
		walk_world(avanza)