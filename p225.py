stores = { "커피음료": 7, "펜": 3, "종이컵": 2, "우유": 8, "콜라": 4, "책": 5 }

sorted_stores = sorted(stores.items(), key=lambda item: item[0])

print(sorted_stores)
