"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from turtle import circle as cc
from freegames import vector


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


# def circle(start, end): # Este es el codigo feo edu
#     # Draw circle from start to end.
#     begin_fill()
#     for i in range(360):
#         up()
#         goto(start.x, start.y)
#         down()
#         forward(((start.y - end.y)**2 + (start.x-end.y)**2)**0.5)
#         right(1)
#     end_fill()


def circle(start, end): # este es el codigo elegante jaja
    # Draw circle from start to end.
    begin_fill()
    radius = ((start.y - end.y)**2 + (start.x-end.y)**2)**0.5
    cc(radius)
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
