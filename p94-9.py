average_speed = float(input("평균 시속(km/h)을 입력하세요: "))
travel_time = float(input("이동 시간(h)을 입력하세요: "))

hours = int(travel_time)
minutes = int((travel_time - hours) * 60)
seconds = int(((travel_time - hours) * 60 - minutes) * 60)

distance = average_speed * travel_time

print(f"평균 시속: {average_speed} km/h")
print(f"이동 시간: {hours} 시간 {minutes} 분 {seconds} 초")
print(f"이동 거리: {distance:.3f} km")
