num = int(input("정수를 입력하세요: "))

if 0 <= num <= 100 and num % 2 == 0:
    print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? True")
else:
    print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False")
