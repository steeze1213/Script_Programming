depth = 30
c_day = 7
s_night = 5
p = 0
day = 1

while p < depth:
    p += c_day
    if p >= depth:
        break
    p -= s_night
    print("day : {:>2} 달팽이의 위치 : {:>2} 미터".format(day, p))
    day += 1

print("축하합니다. 우물을 탈출하였습니다.")
print("우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(day - 1))
