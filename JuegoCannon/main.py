"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
from turtle import *
from freegames import vector

# Vector posicion de pelota
ball = vector(-200, -200)
# Vector velocidad
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Velocidad arbitraria de la pelota
        # Para aumentar sumar por un numero mayor o dividir por uno menor
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()
    # Se grafican y actualizan los Targets existentes
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    # Se actualiza la posicion de nuestro proyectil
    if inside(ball):
        goto(ball.x, ball.y)
        # Forma de proyectil
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    # Target se crea de manera aleatoria
    if randrange(40) == 0:
        # Se establece altura aleatoria en un intervalo
        y = randrange(-150, 150)
        # Posicion inicial de Target
        target = vector(200, y) # 200
        # Se agrega target al array global
        targets.append(target)

    for target in targets:
        # Cada vez si posicion se mueve a la izquierda
        # Restar mayor cantidad para mayor velocidad
        target.x -= 1.0
    
    # La velocidad en y siempre disminuye como gravedad
    if inside(ball):
        speed.y -= 0.7 # Mientras mayo sea, menor sera el tiempo de vuelo
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            target.x = 200 # Una vez que el target llega al final, se regresa al inicio en la x mismo punto en y


    ontimer(move, 50) # 50

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
