s = int(input('시작 정수를 입력하세요 :'))
e = int(input('끝 정수를 입력하세요 :'))

if s>e:
    s,e = e,s
    
sum=0

for i in range(s, e+1):
    sum+=i

print(s, '에서', e, '까지 정수의 합 : ', sum)
