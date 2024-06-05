input_string = input("문자열을 입력하시오: ")

uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

for ch in input_string:
    if ch.isupper():
        uppercase_count += 1
    elif ch.islower():
        lowercase_count += 1
    elif ch.isdigit():
        digit_count += 1
    else:
        special_count += 1

print("대문자, 소문자, 숫자, 특수문자의 수")
print(f"대문자 = {uppercase_count}")
print(f"소문자 = {lowercase_count}")
print(f"숫자 = {digit_count}")
print(f"특수문자 = {special_count}")
