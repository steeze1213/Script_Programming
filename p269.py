s = 'This is a string !@#$%^&*()_+ characters'
result = ''

for ch in s:
    if ch.isalnum():
        result += ch

print(f"원본 문자열: {s}")
print(f"변경된 문자열: {result}")
