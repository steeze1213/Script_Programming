print('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈')
s = int(input('어떤 연산을 원하는지 번호를 입력하세요: '))

if s in [1, 2, 3, 4]:
    x, y = map(int, input('연산을 원하는 숫자 두 개를 입력하세요: ').split())

    if s == 1:
        print(x, '+', y, '=', x+y)

    elif s == 2:
        print(x, '-', y, '=', x-y)

    elif s == 3:
        print(x, '*', y, '=', x*y)

    elif s == 4:
        if y != 0:
            print(x, '/', y, '=', x/y)
        else:
            print('0으로 나눌 수 없습니다.')
    else:
        print('잘못 입력하였습니다.')
else:
    print('잘못 입력하였습니다.')
