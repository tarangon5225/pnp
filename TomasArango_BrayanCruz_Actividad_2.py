'''
Descripcion:Reeborg`s debe encontrar la mitad del mundo,independientemente
de la dimension del mundo, al encontrarla debe colocar una estrella en ella
y devolverse a casa.
pre:El robot inicia en (1,1).
pos:El robot debe estar en su punto de partida es decir casa(1,1)
&& haber dejado la estrella en la mitad del mundo.

Autores: Tomas Arango, Brayan Cruz.
Fecha:05/08/201
'''
'''
Descripcion: funcion medio() Reeborgs contara los pasos
mientras el frente este libre, al llegar a la pared contara
los pasos dados y hallará la mitad de estos, se devolverá 
a la mitad, pondrá la estrella y volverá a casa.
pre:El robot inicia en (1,1).
pos:El robot debe estar en su punto de partida es decir casa(1,1)
'''
def medio ():
    casillas = 1
    #Se mueve mientras el frente está libre
    while front_is_clear():
        move()
        casillas += 1
    mitad = int (casillas/2)
    repeat 2 :
        turn_left()
    while mitad > 0:
        move()
        mitad -= 1
    put("star")
    while front_is_clear():
        move()
medio()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
