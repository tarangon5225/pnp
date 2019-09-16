def turn_180():
	turn_left()
	turn_left()

def turn_right():
	repeat 3:
		turn_left()

def subir_en_L(y,x):
	turn_left()
	while y != 0:
		move()
		y -= 1
	turn_right()
	while x != 0:
		move()
		x -= 1

def rapel():
	move()
	turn_180()
	turn_right()
	while front_is_clear():
		move()
	turn_left()

def recolectar_manzanas():
	manzanas = 0
	if object_here("apple"):
		while object_here():
			take()
			manzanas += 1
	return manzanas
	