PI = 3.141592
radius = float(input("원의 반지름을 입력하세요: "))
circumference = 2 * PI * radius
area = PI * radius ** 2
print("원의 둘레 =", circumference, ", 원의 면적 =", format(area, ".15f"))
