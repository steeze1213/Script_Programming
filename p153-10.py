import turtle
import random

t = turtle.Turtle()

count = 0
while count < 30:
    direction = random.randrange(2)
    if direction == 0:
        t.left(90)
    else:
        t.right(90)
    t.forward(50)
    count += 1

turtle.done()
