pi = 3.14

s_13 = 13
s_22 = 22

r_w = 17
r_l = 25
r_h = 16

c_r = 10
c_h = 15

sp_r = 25

cy_r = 10
cy_h = 15

c_v_13 = s_13 ** 3
c_v_22 = s_22 ** 3

r_v = r_w * r_l * r_h
c_v = (1 / 3) * pi * c_r ** 2 * c_h
sp_v = (4 / 3) * pi * sp_r ** 3
cy_v = pi * cy_r ** 2 * cy_h

print("모서리의 길이가 13인 경우:", c_v_13)
print("모서리의 길이가 22인 경우:", c_v_22)
print("가로, 세로, 길이가 각각 17, 25, 16인 직육면체:", r_v)
print("반지름과 높이가 각각 10, 15인 원뿔:", c_v)
print("반지름이 25인 구:", sp_v)
print("반지름과 높이가 각각 10, 15인 원기둥:", cy_v)
