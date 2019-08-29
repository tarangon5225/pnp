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
    total = 0
    repeat 4:
        subir_escalon()
        total = total + recolectar()
    return total
subir_escalera_sorpresa()
print(recolectar())
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
