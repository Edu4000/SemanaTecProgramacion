from random import *
from turtle import *
from freegames import path


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None, 'numTap':0}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    # Usa coordenadas de la imagen para encontrar indice de hide
    spot = index(x, y)
    # Mark se inicializa en None
    mark = state['mark']
    # Cada tap agrega un numero a la cuenta de taps
    state['numTap'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # Si mark es none se le inicializa asignando un indice que indica un numero
        # Si el indice en mark es igual al nuevo seleccionado se le reasigna el mismo numero
        # Si es el numero es diferente al anterior se le reasigna un nuevo indice
        state['mark'] = spot
    else:
        # Si son distintos indices pero el mismo numero
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        # Se dibujan los cuadros para los tiles que tienen hide = True
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Si todos los tiles estan ocultos. Se acabo el juego
    if not any(hide):

        print("Acabo, felicidades!!")
        print("tu numero de taps fue de:", state['numTap'])
    else:
    # Se actualiza tablero
        update()
        ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()