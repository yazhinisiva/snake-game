from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()

    # Auto move towards food
    if abs(food.x - head.x) > abs(food.y - head.y):  # Prioritize horizontal movement
        if food.x > head.x:
            aim.x, aim.y = 10, 0
        elif food.x < head.x:
            aim.x, aim.y = -10, 0
    else:
        if food.y > head.y:
            aim.x, aim.y = 0, 10
        elif food.y < head.y:
            aim.x, aim.y = 0, -10

    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        print("Game Over! Snake got stuck.")
        return  # Stop the game if stuck or hits wall

    snake.append(head)

    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, 'green')
    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)

hideturtle()
tracer(False)
move()
done()
