import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오: ")
if s == "사각형" :
    s = turtle.textinput("", "가로: ")
    w = int(s)
    s = turtle.textinput("", "세로: ")
    h = int(s)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
elif s == "삼각형":
    s = turtle.textinput("", "한 변의 길이: ")
    sl = int(s)
    for _ in range(3):
        t.forward(sl)
        t.left(120)
elif s == "원":
    s = turtle.textinput("", "반지름: ")
    r = int(s)
    t.circle(r)
turtle.done()
