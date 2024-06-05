stores = { "커피음료": 7, "펜": 3, "종이컵": 2, "우유": 8, "콜라": 4, "책": 5 }

while True:
    print("\n메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료")
    choice = input("메뉴 선택: ")
    
    if choice == '1':
        name = input("[재고조회] 물건의 이름을 입력하시오: ")
        if name in stores:
            print(f"재고: {stores[name]}")
        else:
            print(f"{name}은(는) 목록에 없습니다.")
    
    elif choice == '2':
        entry = input("[입고] 물건의 이름과 수량을 입력하시오: ")
        name, amount = entry.split()
        amount = int(amount)
        if name in stores:
            stores[name] += amount
            print(f"{name}의 재고: {stores[name]}")
        else:
            print(f"{name}은(는) 목록에 없습니다.")
    
    elif choice == '3':
        entry = input("[출고] 물건의 이름과 수량을 입력하시오: ")
        name, amount = entry.split()
        amount = int(amount)
        if name in stores:
            if stores[name] >= amount:
                stores[name] -= amount
                print(f"{name}의 재고: {stores[name]}")
            else:
                print(f"{name}의 재고가 부족합니다. 현재 재고: {stores[name]}")
        else:
            print(f"{name}은(는) 목록에 없습니다.")
    
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("잘못된 입력입니다. 다시 선택하십시오.")
