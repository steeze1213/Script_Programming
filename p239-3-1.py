student_tup = (('241101', '박동윤', '010-1234-4500'), ('241102', '김은지', '010-2230-6540'), ('241103', '이지은', '010-3232-7788'))

student_dict = {}

for student in student_tup:
    student_dict[student[0]] = [student[1], student[2]]

for key, value in student_dict.items():
    print(f"{{'{key}' : {value}}}")
