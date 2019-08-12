'''
Descripción: Reeborg se encuentra en las coordenadas (1,1)
debe llegar a las coordenadas proporcionadas por el usuario y colocar una estrella, regresar 
a casa y al llegar al punto de inicio, decir la distancia que recorrió.
Pre: Reeborg se encuentra en las coordenadas (1,1) con una estrella en el bolsillo,
debe llegar a las coordenadas proporcionadas por el usuario y mira al norte.
Pos: Reeborg debe estar en la coordenada (1,1) después de haber dejado la estrella
en las coordenadas proporcionadas y al terminar decir la distancia que recorrió.
Mundo 10*10
12/08/2019
Tomás Arango Niño
Brayan Cruz Reyes
'''
'''
Descripción: Reeborg utilizará explorar, para llegar a las coordenadas proporcionadas por el usuario.
Pre: Reeborg inicia en las coordenadas (1,1) y está mirando al norte.
pos: Reeborg llega a las coordenadas (1,1) y muestra la distancia desde (1,1) hasta (x,y)
'''
def explorar(x,y):
    contadory = 1
    contadorx = 1
    distancia = 0
    while y > contadory:
        move()
        contadory += 1
    if y == contadory:
        repeat 3:
            turn_left()
    while x > contadorx:
        move()
        contadorx += 1
    if x == contadorx:
        put("star")
        volver_casa()
    distancia = (((x-1)**2)+(y-1)**2)**(1/2)
    print("¡llegué a casa!")
    print("La distancia hasta la estrella fue: ", distancia)
    done()
'''
Descripción: Reeborg retorna a la casa después de haber llegado a la coordenada (x,y)
y haber dejado la estrella en dicha coordenada.
Pre: Reeborg está en la coordenada (x,y) mirando hacia oriente.
Pos: Reeborg está en (1,1) después de haber dejado la estrella en la coordenada indicada por 
el usuario.
'''
def volver_casa():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    
explorar(2,5)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
