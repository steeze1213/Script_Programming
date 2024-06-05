import turtle

turtle.setup(width = 400, height = 400)

myTurtle = turtle.Turtle()
turtle.bgcolor('black')
myTurtle.pencolor('green')
myTurtle.speed(0)
myTurtle.shape('turtle')
myTurtle.shapesize(5, 3)
for i in range(200):
    myTurtle.forward(i)
    myTurtle.left(93)

turtle.done()
