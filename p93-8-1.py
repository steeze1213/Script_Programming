num = int(input("세 자리 정수를 입력하시오: "))

ones_place = num % 10
tens_place = (num // 10) % 10
hundreds_place = num // 100

print(ones_place)
print(tens_place)
print(hundreds_place)
