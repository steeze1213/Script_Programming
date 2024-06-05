student_tup = (('241101', '박동윤', '010-1234-4500'), ('241102', '김은지', '010-2230-6540'), ('241103', '이지은', '010-3232-7788'))

student_id = input("학번을 입력하시오: ")

found = False
for student_info in student_tup:
    if student_info[0] == student_id:
        found = True
        print("이름:", student_info[1])
        print("연락처:", student_info[2])
        break

if not found:
    print("해당하는 학번의 학생이 존재하지 않습니다.")
