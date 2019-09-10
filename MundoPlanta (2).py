'''
Descripción: Reeborg debe recolectar y clasificar todos los elementos encontrados, en el mundo.
Valida cuántos elementos hay en cada casilla y los clasifica en su respectiva lista.
Retorna una lista con los objetos y la cantidad que encontró,
en el orden que los encontró.
Tomás Arango Niño
Brayan Cruz
10-09-2019
'''
objetos_encontrados = []
elemento = "tulip"
'''
Descripción: Reeborg gira a la derecha
Pos: Reeborg gira 270° de la posición inicial
'''
def turn_right():
    repeat 3:
        turn_left()
'''
Descripción: Caminar hacia el frente mientras no encuentre pared.
Antes de avanzar valida si hay elementos, los recoge todos
y los guarda en la lista.
Guarda qué objeto es y la cantidad que encontró.
Pre: Reeborg mira hacia la derecha || mira hacia la izquierda
Pos: Reeborg avanzó hasta donde encontró pared &&
mira hacia la derecha || mira hacia la izquierda
'''
def walk():
    global elemento
    while front_is_clear():
        racimo = recolectar()
        if racimo != 0:
            objetos_encontrados.append([elemento,racimo])
        move()
'''
Descripción: Cambia de fila en el limite derecho del mundo.
Antes de avanzar valida si hay elementos, los recoge todos
y los guarda en la lista.
Guarda qué objeto es y la cantidad que encontró.
Pre: Reeborg está en el X mayor && mira hacia la derecha
Pos: Reeborg está en el X mayor && y+=1 && mira hacia la izquierda
'''
def change_lineR():
    global elemento
    turn_left()
    racimo = recolectar()
    if racimo != 0:
        objetos_encontrados.append([elemento,racimo])
    move()
    turn_left()    
'''
Descripción: Cambia de fila en el limite izquierdo del mundo.
Antes de avanzar valida si hay elementos, los recoge todos
y los guarda en la lista.
Guarda qué objeto es y la cantidad que encontró.
Pre: Reeborg está en x=1 && mira hacia la izquierda
Pos: Reeborg está en x=1 && y+=1 && mira hacia la derecha
'''
def change_lineL():
    global elemento
    turn_right()
    racimo = recolectar()
    if racimo != 0:
        objetos_encontrados.append([elemento,racimo])
    move()
    turn_right()
'''
Descripción: Reeborg avanza por todo el mundo, en zigzag
Pre: Reeborg debe estar en un mundo de 8*8, en la casilla (1,1)
Mirando hacia la derecha
Pos: Reeborg está en la casilla (8,1), retorna la lista con los objetos encontrados.
'''    
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
    return objetos_encontrados
'''
Descripción: Valida si en la casilla hay objetos y los recoge todos.
Retorna el número total de objetos encontrados en la casilla.
Guarda qué objeto encontró en la casilla.
'''    
def recolectar():
    global elemento
    cantidad_elementos = 0
    if object_here("daisy"):
        elemento = "daisy"
        while object_here():
            take()
            cantidad_elementos += 1
    elif object_here("dandelion"):
        elemento = "dandelion"
        while object_here():
            take()
            cantidad_elementos += 1
    elif object_here("leaf"):
        elemento = "leaf"
        while object_here():
            take()
            cantidad_elementos += 1
    else:
        elemento = "tulip"
        while object_here():
            take()
            cantidad_elementos += 1
    return cantidad_elementos        

print(walk_world())
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
