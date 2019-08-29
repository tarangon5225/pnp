puntos = 0
def turn_right():
    repeat 3:
        turn_left()
def subir_escalon():
    turn_left()
    move()
    turn_right()
    move()
def recolectar():
    global puntos
    while front_is_clear():
        if object_here():
            while object_here():
                if object_here("daisy"):
                    take()
                    puntos += 1
                elif object_here("beeper"):
                    take()
                    puntos = puntos * 2
                elif object_here("token"):
                    take()
                    puntos -= 5
        move()
    if object_here():
        while object_here():
            if object_here("daisy"):
                take()
                puntos += 1
            elif object_here("beeper"):
                take()
                puntos = puntos * 2
            elif object_here("token"):
                take()
                puntos -= 5
    return puntos
def subir_escalera_sorpresa():
    repeat 4:
        total = 0
        subir_escalon()
        total = total + recolectar()
    return total
print(subir_escalera_sorpresa())
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
