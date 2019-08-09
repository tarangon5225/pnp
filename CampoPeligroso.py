'''
Descripción: La meta es llegar vivo hasta la casilla (5,5).
Al llegar deberá informar con cuánta energía terminó.
De no conseguirlo, al final de la ejecución debe informar
en qué casilla quedó y la razón de porqué de su fracaso.
Mundo de 5*5
Hecho por: Tomás Arango Niño
Fecha: 09/08/2019
'''
energia = 7
manzana = 7
maleta = 0
token = 0
tulipan = -2
'''
Funcionalidad: Caminar hacia el frente 4 posiciones.
Pre: Reeborg está en x=1 || x=5 && mira hacia la derecha ||
mira hacia la izquierda
Pos: Reeborg está en x=1 || x=5 && mira hacia la derecha ||
mira hacia la izquierda
'''
def walk():
    global energia
    while front_is_clear():
        if energia != 0 :    
            move()
            energia -= 1
        else:
            print("Se acabó la energía")
            done()
'''
Funcionalidad: Cambia de fila en x=5.
Pre: Reeborg está en x=5 && mira hacia la derecha
Pos: Reeborg está en x=5 && y=+1 && mira hacia la izquierda
'''
def change_lineR():
    global energia
    if energia != 0:
        if wall_in_front():
            turn_left()
            move()
            energia -= 1
            turn_left()
    else:
        print("Se acabó la energía")
        done()
'''
Funcionalidad: Cambia de fila en x=1.
Pre: Reeborg está en x=1 && mira hacia la izquierda
Pos: Reeborg está en x=1 && y=+1 && mira hacia la derecha
'''
def change_lineL():
    global energia
    if energia != 0:
        if wall_in_front():
            turn_left()
            turn_left()
            turn_left()
            move()
            energia -= 1
            turn_left()
            turn_left()
            turn_left()
    else:
        print("Se acabó la energía")
        done()
def validar():
    if object_here():
        if object_here("apple"):
            take()
            energia = energia + 7
walk()
change_lineR()
walk()
change_lineL()
walk()
change_lineR()
walk()
change_lineL()
walk()
change_lineR()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
