'''
Descripción: Caminar por el tablero buscando 4 semillas,
recogerlas y plantar 4 margaritas.
Mundo de 5*5
Hecho por: Tomás Arango Niño
Fecha: 02/08/2019
'''
'''
Funcionalidad: Reeborg recoge la semilla y
planta la margarita.
Pre: Reeborg está en (1,1) && mira hacia el este && 
tiene 4 margaritas
Pos: Reeborg está en (1,1) && mira hacia el norte &&
plantó las margaritas && tiene 4 semillas
'''
def plantar():
    take("square")
    put("daisy")
'''
Funcionalidad: Reeborg camina 4 posiciones,
hasta la semilla.
Pre: Reeborg está en (1,1) || (1,5) || (5,5) ||
(5,1) && mira en sentido de la siguiente semilla a recoger
Pos: Reeborg está en (1,1) && mira hacia el norte
'''
def caminar():
    if front_is_clear() :
        repeat 4 :
            move()
        turn_left()
repeat 4:
    caminar()
    plantar()
turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
