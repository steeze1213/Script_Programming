
num = int(input("세 자리 정수를 입력하시오: "))

hundreds_place = num // 100
tens_place = (num // 10) % 10
ones_place = num % 10

print(f"백의 자리: {hundreds_place}")
print(f"십의 자리: {tens_place}")
print(f"일의 자리: {ones_place}")
