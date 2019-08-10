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
tulipan = 1
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
            validar()
        else:
            print("Se acabó la energía")
            print(energia)
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
            validar()
            turn_left()
    else:
        print("Se acabó la energía")
        print(energia)
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
            validar()
            turn_left()
            turn_left()
            turn_left()
    else:
        print("Se acabó la energía")
        print(energia)
        done()
'''
Funcionalidad: Reeborg valida qué hay en cada espacio
al que avanza, y según qué encuentre hace la respectiva
acción.
Pre:
Pos:
'''
def validar():
    global energia
    global tulipan
    global manzana
    global maleta
    global token
    if object_here():
        if energia == 14:
            if maleta != 0:
                while maleta != 0:
                    energia = energia + manazana
                    maleta -= 1
        elif object_here("apple"):
            take("apple")
            if energia > 20:
                maleta += 1
            else:
                energia = energia + manzana
        elif object_here("triangle"):
            take("triangle")
            if carries_object("tulip"):
                energia = energia * 2
            else:
                tulipan = 0
        elif object_here("tulip"):
            if carries_object("triangle"):
                take("tulip")
            else:
                take("tulip")
                tulipan = tulipan * 2
                energia = int(energia/tulipan)
        elif object_here("token"):
            take("token")
            while maleta != 0:
                put("apple")
                maleta -= 1
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
