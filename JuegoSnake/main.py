"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange, choice
from freegames import square, vector

import random
colorIndexS = random.randint(0,4)
colorIndexF = random.randint(0,4)

while colorIndexF == colorIndexS:
    colorIndexF = random.randint(0, 4)

colorS = ['green', 'black', 'blue', 'yellow', 'brown']
colorF = ['green', 'black', 'blue', 'yellow', 'brown']

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190 # Boundaries defined as the range of the board


def move():
    "Move snake forward one segment."
    head = snake[-1].copy() # posicion antes de moverse
    head.move(aim) # posicion despues de moverse
    food.move(vector(choice([-10, 0, 10]), choice([-10, 0, 10])))

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    elif not inside(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    snake.append(head) # vector de [pos antes, pos despues]

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0) # Se actualiza el vector y se queda la posicion de despues

    clear()
    # seccion de dibujo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, colorS[colorIndexS])

    square(food.x, food.y, 9, colorF[colorIndexF])
    update()
    ontimer(move, 75) # Velocidad con la que se mueve la serpiente


setup(420, 420, 370, 0) # in pixels
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()