num = int(input("세 자리 정수를 입력하시오: "))

hundreds_place = num // 100
tens_place = (num // 10) % 10
ones_place = num % 10

print(f"{ones_place}{tens_place}{hundreds_place}")
