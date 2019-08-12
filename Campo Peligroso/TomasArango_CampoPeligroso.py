'''
Descripción: La meta es llegar vivo hasta la casilla (5,5).
Al llegar deberá informar con cuánta energía terminó.
De no conseguirlo, al final de la ejecución debe informar
la razón de porqué de su fracaso.
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
    global manzana
    global maleta
    global tulipan
    while front_is_clear():
        if tulipan <= energia:
            if energia != 0 :
                move()
                if tulipan != 0:
                    energia = energia - tulipan    
                else:
                    energia -= 1
                validar()
            elif energia == 0:
                if maleta != 0:
                    while maleta != 0:
                        energia = energia + manzana
                        maleta -= 1
                        print("me comí una manzana de la maleta")
                else:
                    print("Se acabó la energía")
                    print(energia)
                    done()
            else:
                print("Se acabó la energía")
                print(energia)
                done()
        else:
            print("No puedo más")
            print("Dar un paso cuesta")
            print(tulipan)
            print("Tengo esta energia: ")
            print(energia)
            done()
'''
Funcionalidad: Cambia de fila en x=5.
Pre: Reeborg está en x=5 && mira hacia la derecha
Pos: Reeborg está en x=5 && y=+1 && mira hacia la izquierda
'''
def change_lineR():
    global energia
    global manzana
    global maleta
    global tulipan
    if tulipan <= energia:
        if energia != 0:
            if wall_in_front():
                turn_left()
                move()
                if tulipan != 0:
                    energia = energia - tulipan    
                else:
                    energia -= 1
                validar()
                turn_left()
        elif energia == 0:
            if maleta != 0:
                while maleta != 0:
                    energia = energia + manzana
                    maleta -= 1
                    print("me comí una manzana de la maleta")
            else:
                print("Se acabó la energía")
                print(energia)
                done()
        else:
            print("Se acabó la energía")
            print(energia)
            done()
    else:
        print("No puedo más")
        print("Dar un paso cuesta")
        print(tulipan)
        print("Tengo esta energia: ")
        print(energia)
        done()    
'''
Funcionalidad: Cambia de fila en x=1.
Pre: Reeborg está en x=1 && mira hacia la izquierda
Pos: Reeborg está en x=1 && y=+1 && mira hacia la derecha
'''
def change_lineL():
    global energia
    global manzana
    global maleta
    global tulipan
    if tulipan <= energia:
        if energia != 0:
            if wall_in_front():
                turn_left()
                turn_left()
                turn_left()
                move()
                if tulipan != 0:
                    energia = energia - tulipan    
                else:
                    energia -= 1
                validar()
                turn_left()
                turn_left()
                turn_left()
        elif energia == 0:
            if maleta != 0:
                while maleta != 0:
                    energia = energia + manzana
                    maleta -= 1
                    print("me comí una manzana de la maleta")
            else:
                print("Se acabó la energía")
                print(energia)
                done()
        else:
            print("Se acabó la energía")
            done()
    else:
        print("No puedo más")
        print("Dar un paso cuesta")
        print(tulipan)
        print("Tengo esta energia: ")
        print(energia)
        done()
'''
Funcionalidad: Reeborg valida qué hay en cada espacio
al que avanza, y según qué encuentre hace la respectiva
acción.
Pre: El objeto que debe haber en la casilla solamente puede ser
apple, triangule, tulip o token, sino es uno de estos objetos
Reeborg solo valida que hay algo en la casilla.
Pos: Reeborg recogió el objeto que encontró (solo de los específicos)
y realizó la acción indicada según el objeto.
'''
def validar():
    global energia
    global tulipan
    global manzana
    global maleta
    global token
    if object_here():
        if object_here("apple"):
            take("apple")
            if energia > 14:
                maleta += 1
                print("Guardé una manzana en la maleta")
            else:
                energia = energia + manzana
        elif object_here("triangle"):
            take("triangle")
            tulipan = 0
        elif object_here("tulip"):
            take("tulip")
            if carries_object("triangle"):
                tulipan = 0
            else:
                tulipan = tulipan * 2
        elif object_here("token"):
            take("token")
            while maleta != 0:
                put("apple")
                maleta -= 1
repeat 2:
    walk()
    change_lineR()
    walk()
    change_lineL()
walk()
print("¡Llegué a la meta! Mi energía es:")
print(energia)
done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
