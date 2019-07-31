'''
Descripción: Caminar por el tablero buscando una manzana,
recogerla y regrese a casa.
Mundo de 5*5
Hecho por: Tomás Arango Niño
Fecha: 31/07/2019
'''
'''
Funcionalidad: Caminar hacia al frente 4 posiciones
buscando la manzana.
Pre: Reeborg está en x=1 && mira hacia la derecha
Pos: Reeborg está en x=5 && mira hacia la derecha
'''
def search_line():
    if front_is_clear() :
        repeat 4 :
            if object_here() :
                take()
                return_home()
            else:
                move()
'''
Funcionalidad: Cambia de fila en x=5.
Pre: Reeborg está en x=5 && mira hacia la derecha
Pos: Reeborg está en x=5 && y=+1 && mira hacia la izquierda
'''
def change_lineR():
    if wall_in_front():
        turn_left()
        move()
        turn_left()
'''
Funcionalidad: Cambia de fila en x=1.
Pre: Reeborg está en x=1 && mira hacia la izquierda
Pos: Reeborg está en x=1 && y=+1 && mira hacia la derecha
'''
def change_lineL():
    if wall_in_front():
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
'''
Funcionalidad: Regresa a la casa con la manzana,
después de haberla encontrado.
Pre: Reeborg está en (1,1)
Pos: Reeborg está en (5,1) || Reeborg está en (1,5)
'''
def return_home():
    repeat 10 :
        if is_facing_north() :
            turn_left()
            repeat 4 :
                if front_is_clear() :
                    move()
                else:
                    turn_left()
                    if at_goal() :
                        done()
                    else:
                        move()
        else:
            turn_left()
        
search_line()
change_lineR()
search_line()
change_lineL()
search_line()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
