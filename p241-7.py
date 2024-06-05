mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

a, b = map(int, input("두 정수를 입력하시오: ").split())

if (a, b) in mylist:
    index = mylist.index((a, b)) + 1
    print(f"{index}번째에 ({a}, {b}) 요소가 있습니다.")

elif (b, a) in mylist:
    index = mylist.index((b, a)) + 1
    print(f"({a}, {b}) 요소는 없으나 {index}번째에 ({b}, {a}) 요소가 있습니다.")
else:
    print("이 요소는 없습니다.")
