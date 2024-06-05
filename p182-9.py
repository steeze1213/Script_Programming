import math

def area_and_circumference(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area, circumference

while True:
    r = float(input("반지름을 입력하시오 (-1이 입력되면 종료): "))
        
    if r == -1:
        print("프로그램을 종료합니다.")
        break
        
    if r < 0:
        print("음수가 입력되었습니다. 프로그램을 종료합니다.")
        break
        
    area, circumference = area_and_circumference(r)
    print(f"넓이: {area:.3f}, 둘레: {circumference:.3f}")
