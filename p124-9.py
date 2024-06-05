import turtle

left_bottom_x, left_bottom_y = map(int, turtle.textinput("", "왼쪽 하단 모서리 좌표 x, y: ").split())
right_top_x, right_top_y = map(int, turtle.textinput("", "오른쪽 상단 모서리 좌표 x, y: ").split())
point_x, point_y = map(int, turtle.textinput("", "점의 좌표 x, y: ").split())

screen = turtle.Screen()
screen.setup(width=300, height=400)
screen.setworldcoordinates(left_bottom_x - 1, left_bottom_y - 1, right_top_x + 1, right_top_y + 1)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()

t.goto(left_bottom_x, left_bottom_y)
t.pendown()

t.goto(right_top_x, left_bottom_y)
t.goto(right_top_x, right_top_y)
t.goto(left_bottom_x, right_top_y)
t.goto(left_bottom_x, left_bottom_y)

t.penup()
t.goto(point_x, point_y)
t.dot(50, "black")

if left_bottom_x <= point_x <= right_top_x and left_bottom_y <= point_y <= right_top_y:
    t.write("점은 사각형의 내부에 있습니다.", align="left")
else:
    t.write("점은 사각형의 외부에 있습니다.", align="left")

screen.mainloop()
