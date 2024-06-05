height = int(input('숫자를 입력하세요: '))

print("첫 번째 삼각형:")
for i in range(1, height + 1):
    print('*' * i)

print("\n두 번째 삼각형:")
for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * i)

print("\n세 번째 삼각형:")
for i in range(height, 0, -1):
    print(' ' * (height - i) + '*' * i)

print("\n네 번째 삼각형:")
for i in range(height, 0, -1):
    print('*' * i)
