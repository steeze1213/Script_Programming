'''
result = ""
for i in range(1, 101):
    if i & 1:
        result += "%d, " % i
print('1에서 100까지의 수 중에서 홀수는 :',result[0:len(result)-2])

result = ""
i = 1

while i <= 100:
    if i % 2 != 0:
        result += "%d, " % i
    i += 1

print('1에서 100까지의 수 중에서 홀수는 :', result[0:len(result)-2])

result = ""

for i in range(1, 101):
    if i % 2 == 0:
        result += "%d, " % i

print('1에서 100까지의 수 중에서 짝수는:', result[0:len(result)-2])
'''
result = ""
i = 1

while i <= 100:
    if i % 2 == 0:
        result += "%d, " % i
    i += 1

print('1에서 100까지의 수 중에서 짝수는:', result[0:len(result)-2])
