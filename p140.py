import turtle
t = turtle.Turtle()
t.shape("turtle")
i = 1
n = 1
 
while i <= 10:
    t.forward(50)
    if i == n * 2 - 1:
        t.left(72)
        i = i + 1
 
    elif i == n * 2:
        t.right(144)
        i = i + 1
        n = n + 1
