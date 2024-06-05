import math

x1 = float(input("x1 좌표를 입력하시오: "))
y1 = float(input("y1 좌표를 입력하시오: "))
x2 = float(input("x2 좌표를 입력하시오: "))
y2 = float(input("y2 좌표를 입력하시오: "))

base = abs(x2 - x1)
height = abs(y2 - y1)

area = (base * height) / 2

print(f"직각삼각형의 면적은: {area}")
