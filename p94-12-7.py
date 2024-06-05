import math

c_r = 10
c_h = 15
c_v = (1 / 3) * math.pi * c_r ** 2 * c_h
print(f"반지름과 높이가 각각 10, 15인 원뿔: {c_v}")

sp_r = 25
sp_v = (4 / 3) * math.pi * sp_r ** 3
print(f"반지름이 25인 구: {sp_v}")

cy_r = 10
cy_h = 15
cy_v = math.pi * cy_r ** 2 * cy_h
print(f"반지름과 높이가 각각 10, 15인 원기둥: {cy_v}")
