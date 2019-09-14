'''
Descripción: Nos encontramos con un juego muy conocido por todos denominado escalerita en un mundo de 12*12, donde se enfrentarán
los jugadores atravesando por todo el mundo encontraran ayudas o dificultades para llegar a la meta, avanzaran de manera
escalonada por filas, hasta llegar a su meta.

LAS REGLAS SON:

1) Será considerado ganador, el primer jugador en llegar a la meta casilla (1,12).
2) Para iniciar se lanzará un dado, quien saque el mayor número iniciará la partida.
3) Solo será un turno de movimiento y posteriormente pasará el turno, el siguiente jugador hará lo mismo.
4) El jugador que robe turno, será penalizado perdiendo su siguiente turno.

AYUDAS Y TRAMPAS:

- BEEPER: Si reeborg se detiene sobre un Beeper, automáticamente este será impulsado por su fuerza y podrá subir una fila.
- TULIPAN: Cuando Reeborg se detiene sobre un tulipán él lo come generando una confusión de donde se encuentra, da un giro de
    180° y se regresará las casillas avanzadas.
- TRIANGULO: Si Reeborg para encima de un trangulo, este afectara sus sentidos y hara que baje una linea.

Autores: Brayan Cruz - Tomás Arango
Fecha de entrega:18/09/2019
'''
'''
Descripción: Esta función se usa con el fin de utilizar los robots
que sean necesarios, dependiendo a la cantidad de reeborgs que vamos a usar, se puede como máximo 4 jugadores
'''

r1 = UsedRobot()
r2 = UsedRobot()
r3 = UsedRobot()
r4 = UsedRobot()

'''
Descripción: Esta función se usa cuando Reeborg se encuentra en el extremo derecho del mundo
y necesita subir de fila, para seguir con su camino en el mapa.
Pre: Reeborg se encuentra en el extremo derecho del mapa mirando al este.
Pos: Reeborg estará en la fila de arriba en el extremo derecho, pero mirando al oeste.

'''
sub_dere_arri():
    turn_left()
    move()
    turn_left()
   
'''
Descripción: Con esta función, Reeborg girara hasta dar toda la vuelta y estar mirando
a la derecha de acuerdo de donde se encuentre.

'''

turn_right():
    repeat 3 :
        turn left()
   
'''
Descripción: esta variable se usa cuando Reeborg se encuentra en el extremo izquierdo del mundo
y necesita subir de fila, para seguir con su camino en el mapa.
Pre: Reeborg se encuentra en el extremo izquierdo del mapa mirando al este.
Pos: Reeborg estará en la fila de arriba en el extremo izquierdo, pero mirando al oeste.

'''
sub_izqui_arrib():
    turn_right()
    move()
    turn_right()
   
'''
Descripcion:Usamos esta funcion cuando nesecitamos que Reeborg haga un giro de 180ª

'''
       
giro_180():
    repeat 2 :
        turn_left()
'''
"beeper"
Descripcion:Esta es una ayuda que presentara el jugador si se cae en el bepper
podra subir de fila lo cual sera un atajo.
'''
if object_here("beeper"):
    while Beppered()
   
   
Beppered():
    sub_dere_arri()#Solo colocar en fila impar#
   

'''
"tulip"
Descripcion:Cuando Reeborg se para encima de un tulipán él lo come generando una confusión de donde se encuentra, da un giro de
180° y se moverá por un turno en la dirección contraria.
'''
tulipan():
    giro_180()
    move(variable)
    giro_180()
   
   
'''
"triangle"
Descripcion:Si Reeborg para encima de un trangulo, este afectara sus sentidos y hara que
baje una linea y tenga desventaja ante su compañero.

'''
Triangulo():
    turn_left()
    move()
    turn_left()

   
'''
IMPAR: VA A LA DERECHA
PAR: A LA IZQUIERDA
'''
