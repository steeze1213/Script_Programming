fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

max_length = max(len(fruit) for fruit in fruit_list)
longest_fruits = [fruit for fruit in fruit_list if len(fruit) == max_length]

print("가장 길이가 긴 문자열:", ', '.join(longest_fruits))

for fruit in longest_fruits:
    fruit_list.remove(fruit)

print("fruit_list =", fruit_list)
