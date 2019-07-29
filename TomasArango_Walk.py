'''
Descripción: Caminar por el tablero, bajo condiciones.
Mundo de 5*5
Hecho por: Tomás Arango Niño
Fecha: 29/07/2019
'''
'''
Funcionalidad: Caminar recto la cantidad de veces definida.
Pre: Reeborg está en (1,1)
Pos: Reeborg está en (5,1) || Reeborg está en (1,5)
'''
def walk():
    if front_is_clear() :
        repeat 4 :
            move()
'''
Funcionalidad: Caminar en zigzag hasta la posición definida.
Pre: Reeborg está en (1,1) && Reeborg camina hacia el Norte
Pos: Reeborg está en (5,5) && Reeborg camina hacia el Norte
'''          
def walk_zigzag():
    repeat 4 :
        move()
        repeat 3 :
            turn_left()
        move()
        turn_left()
walk_zigzag()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
