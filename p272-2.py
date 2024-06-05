input_string = input("문자열을 입력하시오: ")

lowercase_chars = ""
uppercase_chars = ""

for ch in input_string:
    if ch.islower():
        lowercase_chars += ch
    elif ch.isupper():
        uppercase_chars += ch

modified_string = lowercase_chars + uppercase_chars
print(f"수정된 문자열: {modified_string}")
