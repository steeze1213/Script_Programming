'''
s = "IT's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAM IN COVID!!!"

print(f"입력={s}")
count = 0
for word in s.split():
    if( word == word.upper() ):
        count += 1
print(f"\n대문자 단어의 수={count}")
t = s.lower()
t = t.replace('!',"");
t = t.replace('.',"");
t = t.replace("'","");
print(f"결과={t}")
'''
s = "IT's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAM IN COVID!!!"

exclamation_count = s.count('!')

uppercase_count = sum(1 for ch in list(s) if ch.isupper())

print(f"입력={s}")
print(f"느낌표 갯수 : {exclamation_count}")
print(f"대문자 갯수 : {uppercase_count}")
