s = input("문자열을 입력하세요: ")

length = len(s)

for i in range(length * 2 - 1):
    if i < length:
        print(s[:i + 1])
    else:
        print(s[:length * 2 - i - 1])
