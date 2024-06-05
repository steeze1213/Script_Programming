import math

x1 = float(input("x1 좌표를 입력하시오: "))
y1 = float(input("y1 좌표를 입력하시오: "))
x2 = float(input("x2 좌표를 입력하시오: "))
y2 = float(input("y2 좌표를 입력하시오: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"두 점의 거리: {distance}")
