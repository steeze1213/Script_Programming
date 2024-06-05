import random

me = list(map(int, input('세 복권번호를 입력하시오 : ').split()))
alist = []

for i in range(3):
    lotto = random.randint(0, 9)
    print("당첨번호는", lotto, "입니다.")
    alist.append(lotto)

count = 0
for num in me:
    if num in alist:
        count += 1

if count == 1:
    print("상금 1만원")
elif count == 2:
    print("상금 1천만원")
elif count == 3:
    print("상금 1억원")
else:
    print("다음 기회에...")
