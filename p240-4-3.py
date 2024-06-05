from collections import Counter

lst = [10, 30, 40, 50, 30, 30, 20, 20, 20, 10, 30]
frequency = Counter(lst)

for item, count in frequency.items():
    if count > 1:
        print(f"{item} : {count} 회")
