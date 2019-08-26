'''
Descripción: Reeborg se mueve horizontal o verticalmente en linea recta
en un campo de 8*8 de ajedrez, desde cualquier posición, 
según una direccion y el número de pasos a avanzar

Pre: Recibe dos enteros:
    - direccion: que indica hacia qué dirección se mueve Reeborg.
        1 <= direccion <= 4
    - avanzar: que indica cuántas posiciones se va a mover Reeborg.
        1 <= avanzar <= 8
Reeborg debe mirar al norte

Pos: Reeborg llega la posición deseada y retorna verdadera
Reeborg se retorna a la posición de inicio y retorna false
Reeborg mira al norte
Si encuentra un objeto, se devuelve a su posición de inicio y retorna falso.
Si puede moverse retorna verdadero.

direccion = 1 = arriba
direccion = 2 = izquierda
direccion = 3 = abajo
direccion = número entero = derecha

fecha:
23/08/2019
autores:
Daniel Hernández
Sebastian Trujillo
Tomás Arango

'''

def giro_derecha() :
    repeat 3:
        turn_left()

def giro_180():
    turn_left()
    turn_left()
    
def mueve_torre(direccion, avanzar):
    contador = 0
    bloqueo = True
    if direccion == 1:
        while avanzar != 0:
            move()
            contador += 1
            avanzar -= 1
            if object_here():
                giro_180()
                while contador != 0:
                    move()
                    contador -= 1
                giro_180()
                bloqueo = False
        return bloqueo
    elif direccion == 2:
        turn_left()
        while avanzar != 0:
            move()
            contador += 1
            avanzar -= 1
            if object_here():
                giro_180()
                while contador != 0:
                    move()
                    contador -= 1
                turn_left()
                bloqueo = False
            else:
                if avanzar == 0: 
                    giro_derecha()
        return bloqueo
    elif direccion == 3:
        giro_180()        
        while avanzar != 0:
            move()
            contador += 1
            avanzar -= 1
            if object_here():
                giro_180()
                while contador != 0:
                    move()
                    contador -= 1
                bloqueo = False
            else:
                if avanzar == 0: 
                    giro_180()
        return bloqueo
    else: 
        giro_derecha()
        while avanzar != 0:
            move()
            contador += 1
            avanzar -= 1
            if object_here():
                giro_180()
                while contador != 0:
                    move()
                    contador -= 1
                giro_derecha()
                bloqueo = False
            else:
                if avanzar == 0: 
                    turn_left()
        return bloqueo

print(mueve_torre(4,3))
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
