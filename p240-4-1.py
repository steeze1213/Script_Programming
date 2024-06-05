from collections import Counter

lst = [10, 30, 40, 50, 30, 30, 20, 20, 20, 10, 30]
counter = Counter(lst)
non_duplicates = [key for key, value in counter.items() if value == 1]

print("중복이 없는 원소:", non_duplicates)
