"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector
import math


def line(start, end):
    # Draw line from start to end.
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    # Draw square from start to end.
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        right(90)

    end_fill()


def circle(start, end):
    centerX = start.x + (end.x - start.x)/2
    centerY = start.y + (end.y - start.y)/2
    radius = math.sqrt((end.x-start.x)**2+(end.y-start.y)**2)/2
    up()
    pos_X = radius * math.cos(math.radians(0)) + centerX
    pos_Y = radius * math.sin(math.radians(0)) + centerY
    goto(pos_X, pos_Y)
    down()
    begin_fill()
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

    for count in range(2):
        forward(end.x - start.x)
        right(90)
        forward((end.x - start.x)/2)
        right(90)

    end_fill()


def triangle(start, end):
    # Draw triangle from start to end.
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    forward(end.y - end.x)
    goto(end.x, end.y)
    goto(start.x, start.y)
    end_fill()


def tap(x, y):
    # Store starting point or draw shape.
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    # Store value in state at key.
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
speed(0)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
