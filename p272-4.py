a = "ABCD"
b = "1234"

new_str1 = ''.join([a[i] + b[i] for i in range(len(a))])
new_str2 = ''.join([a[i] + b[len(b) - 1 - i] for i in range(len(a))])

print(f"a = {a}")
print(f"b = {b}")
print(f"new_str1 = {new_str1}")
print(f"new_str2 = {new_str2}")
