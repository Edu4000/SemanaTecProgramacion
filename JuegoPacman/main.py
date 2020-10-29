from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False) # pacman
writer = Turtle(visible=False) # comida de pacman
aim = vector(5, 0) # dirección hacia donde se mueve
pacman = vector(-40, -80) # valor inicial de pacman (spawnpoint)


# spawnpoint de fantasmas con direccion inicial
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Lista de pasillos
auxList = [[21, 22, 23, 24, 25, 26, 27, 0], [29, 30, 31, 32, 33, 34, 35, 0],
           [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 0],
           [101, 102, 103, 104, 0], [106, 107, 0], [109, 110, 0], [112, 113, 114, 115, 0],
           [146, 147, 148, 149, 150, 0], [161, 162, 163, 164, 165, 166, 0], [170, 171, 172, 173, 174, 175, 0],
           [186, 187, 188, 189, 190, 0], [221, 222, 223, 224, 225, 226, 227, 0], [229, 230, 231, 232, 233, 234, 235, 0],
           [261, 262, 0], [264, 265, 266, 267, 268, 269, 270, 271, 272, 0], [274, 275, 0],
           [301, 302, 303, 304, 0], [306, 307, 0], [309, 310, 0], [312, 313, 314, 315, 0],
           [341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 0],
           [21, 41, 61, 81, 101, 121, 141, 161, 1], [221, 241, 261, 1], [301, 321, 341, 1], [262, 282, 302, 1],
           [24, 44, 64, 84, 104, 124, 144, 164, 184, 204, 224, 244, 264, 284, 304, 1], [66, 86, 106, 1],
           [146, 166, 186, 206, 226, 1], [266, 286, 306, 1], [27, 47, 67, 1], [107, 127, 147, 1], [227, 257, 267, 1], [307, 327, 347, 1],
           [29, 49, 69, 1], [109, 129, 149, 1], [229, 249, 269, 1], [309, 329, 349, 1], [310, 290, 270, 1], [150, 170, 190, 210, 230, 1],
           [110, 90, 70, 1], [32, 52, 72, 92, 112, 132, 152, 172, 192, 212, 232, 1], [272, 292, 312, 1], [274, 294, 314, 1],
           [315, 335, 355, 1], [175, 195, 215, 235, 255, 275, 1], [35, 55, 75, 95, 115, 1]]


def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4): #  Se genera el tablero
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20 # 200
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])
    clear()
    pursuit = False

    if valid(pacman + aim): # Si el movimiento es posible, moverse
        pacman.move(aim)

    indexP = offset(pacman) # indice del objeto. El indice se encuentra por una transformada del plano con respecto a la matriz.

    if tiles[indexP] == 1: # Si el indice esta lleno, entonces ese indice se vuelve 2 y ya no esta lleno
        tiles[indexP] = 2
        state['score'] += 1 # se le agrega al score
        x = (indexP % 20) * 20 - 200
        y = 180 - (indexP // 20) * 20
        square(x, y) # se pinta el square

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        indexF = offset(point)  # Index de un fantasma
        for corridor in auxList:  # 0 fila, 1 columna
            if indexF in corridor and indexP in corridor:
                if indexF > indexP and corridor[-1] == 0:
                    course.x = vector(-5, 0).x
                    course.y = vector(-5, 0).y

                elif indexF > indexP and corridor[-1] == 1:
                    course.x = vector(0, 5).x
                    course.y = vector(0, 5).y

                elif indexF < indexP and corridor[-1] == 0:
                    course.x = vector(5, 0).x
                    course.y = vector(5, 0).y

                elif indexF < indexP and corridor[-1] == 1:
                    course.x = vector(0, -5).x
                    course.y = vector(0, -5).y

        if valid(point + course): # Si el rumbo actual es valido, moverse
            point.move(course)
        else:
            options = [
                vector(5, 0), # Right
                vector(-5, 0), # Left
                vector(0, 5), # Up
                vector(0, -5), # Down
            ]
            plan = choice(options) # Random.choice
            course.x = plan.x # se actualiza el curso con alguna opcion aleatoria en x y y
            course.y = plan.y

        up()
        goto(point.x + 12, point.y + 12) # se mueve y dibuja
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 50)


def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
