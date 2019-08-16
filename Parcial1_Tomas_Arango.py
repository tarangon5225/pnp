'''
Descripción: Reeborg va caminar sobre el eje y en x=1, buscando la y que se ingresa por parámetros,
luego va a poner cuantas estrellas se defina en el limite, por parámetros, en el eje x. Por último, retornará
a casa (1,1).
Tomás Arango Niño
16/08/2019
'''
'''
Descripción: Reeborg gire a la derecha, sin importar la dirección en la que esté.
Pre: 
Pos: Reeborg giró a la derecha, de su posición inicial.
'''
def turn_right():
    repeat 3 :
        turn_left()
'''
Descripción: Reeborg gire 180 grados, sin importar la dirección en la que esté.
Pre:
Pos: Reeborg giró 180 grados de su posición inicial.
'''
def turn_180():
    turn_left()
    turn_left()
'''
Descripción: Reeborg va desde (1,1) hasta (1,y) y pone en cada casilla una estrella hasta 
llegar a la posición (limit,y).
Pre: Reeborg está en (1,1). Recibe dos números enteros tales que:    1<y<=limit<=10
Pos: Reeborg está en (limit,y) y mira al este.
'''
def draw_a_line(y, limit):
    contadorx = 1
    contadory = 1
    #Mira si Reeborg está en la primera casilla y debe poner estrellas en es y
    if y == 1 :
        #Pone estrellas hasta el límite
        while contadorx <= limit:
            put("star")
            #Si el frente está despejado se mueve
            if front_is_clear():
                move()
            contadorx += 1
    turn_left()
    #Se mueve hasta que llegué al y deseado
    while contadory < y :
        move()
        contadory += 1
    turn_right()
    #Pone estrellas hasta el límite
    while contadorx <= limit:
            put("star")
            #Si el frente está despejado se mueve
            if front_is_clear():
                move()
            contadorx += 1
    go_back_home()
'''
Descripción: Desde su posición actual, Reeborg va hasta la casilla (1,1) y termina mirando en sentido Este. 
Pre: Reeborg mira al este.
Pos: Reeborg está en (1,1) y mira al este.
'''  
def go_back_home():
    turn_180()
    #Mientras el frente esté despejado se mueve
    while front_is_clear():
        move()
    turn_left()
    #Mientras el frente esté despejado se mueve
    while front_is_clear():
        move()
    turn_left()
    
draw_a_line(3,1)
draw_a_line(4,4)
draw_a_line(6,10)
draw_a_line(8,5)
draw_a_line(9,2)
        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
