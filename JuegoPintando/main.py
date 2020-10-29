from turtle import *
from freegames import vector
import math


def line(start, end):
    # Draw line from start to end.
    up()
    # Inicio en start
    goto(start.x, start.y)
    down()
    # Linea recta que termina en end
    goto(end.x, end.y)


def square(start, end):
    # Draw square from start to end.
    up()
    # Se empieza desde el punto start
    goto(start.x, start.y)
    down()
    begin_fill()

    # For para los cuatro lados de un cuadrado
    for count in range(4):
        # Se mueve la diferencia de x start y final
        # (constantel por tener lados iguales)
        forward(end.x - start.x)
        # Vueltas de 90 grados para crear forma
        right(90)

    end_fill()

# Los puntos del inicio y final puntos opuestos en perimetro del circulo
def circle(start, end):
    # Funciones para encontrar punto medio de circulo : Centro
    centerX = start.x + (end.x - start.x)/2
    centerY = start.y + (end.y - start.y)/2
    # Distancia euclidiana entre el centro y la circunferencia : Radio
    radius = math.sqrt((end.x-start.x)**2+(end.y-start.y)**2)/2
    up()
    # Cada posicion del circulo se define apartir de la definicion de un circulo en el plano polar
    pos_X = radius * math.cos(math.radians(0)) + centerX
    pos_Y = radius * math.sin(math.radians(0)) + centerY
    goto(pos_X, pos_Y) # El trazo se mueve a nueva posicion
    down()
    begin_fill()
    # For para cambiar entre los 360 grados de un circulo
    for i in range(359):
        posX = radius * math.cos(math.radians(1+i)) + centerX
        posY = radius * math.sin(math.radians(1+i)) + centerY
        goto(posX, posY)
        down()

    end_fill()
    

def rectangle(start, end):
    # Draw rectangle from start to end.
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Contador para los dos lados del rectangulo
    for count in range(2): # contador para los dos lados del rectangulo
        # Lado de x
        forward(end.x - start.x)
        right(90)
        # Lado de y
        forward(end.y - start.y)
        right(90)

    end_fill()


def triangle(start, end):
    # Draw triangle from start to end.
    up()
    # Inicio coordenada start
    goto(start.x, start.y)
    down()
    # Linea recta a punto x de end y mismo punto y
    begin_fill()
    goto(end.x, start.y)
    # Linea recta a punto medio entre start y end x con altura end.y
    down()
    goto(start.x - (start.x - end.x) / 2, end.y)
    # Regreso a punto inicial
    down()
    goto(start.x, start.y)
    end_fill()


def tap(x, y):
    # Store starting point or draw shape.
    start = state['start']

    if start is None:
        # Guardar start
        state['start'] = vector(x, y)
    else:
        # Guardar end
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    # Store value in state at key.
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap) # Identificar coordenadas de click
speed(0)
listen() # Lector de interacciones
onkey(undo, 'u') # Deshacer
# Seleccion y cambio de colores con teclas (Importante block mayus)
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
# Seleccion y cambio de forma dibujada con teclas
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
