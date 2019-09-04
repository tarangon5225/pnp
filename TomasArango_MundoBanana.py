bananas = []
def turn_right():
    repeat 3:
        turn_left()
'''
Funcionalidad: Caminar hacia el frente 4 posiciones.
Pre: Reeborg está en x=1 || x=5 && mira hacia la derecha ||
mira hacia la izquierda
Pos: Reeborg está en x=1 || x=5 && mira hacia la derecha ||
mira hacia la izquierda
'''
def walk():
    while front_is_clear():
        racimo = recolectar_bananas()
        if racimo != 0:
            bananas.append(racimo)
        move()
'''
Funcionalidad: Cambia de fila en x=5.
Pre: Reeborg está en x=5 && mira hacia la derecha
Pos: Reeborg está en x=5 && y=+1 && mira hacia la izquierda
'''
def change_lineR():
    turn_left()
    racimo = recolectar_bananas()
    if racimo != 0:
        bananas.append(racimo)
    move()
    turn_left()    
'''
Funcionalidad: Cambia de fila en x=1.
Pre: Reeborg está en x=1 && mira hacia la izquierda
Pos: Reeborg está en x=1 && y=+1 && mira hacia la derecha
'''
def change_lineL():
    turn_right()
    racimo = recolectar_bananas()
    if racimo != 0:
        bananas.append(racimo)
    move()
    turn_right()
    
def walk_world():
    think(1)
    repeat 3:
        walk()
        change_lineR()
        walk()
        change_lineL()
    walk()
    change_lineR()
    walk()
    return bananas
    
def recolectar_bananas():
    num_bananas = 0
    while object_here("banana"):
        take("banana")
        num_bananas += 1
    return num_bananas
    
    
print(walk_world())
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
