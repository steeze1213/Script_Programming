student_tuple = [('241101', '강이안', '010-123-1111'), 
                 ('241102', '박동민', '010-123-2222'), 
                 ('241103', '김수정', '010-123-3333')]

student_dict = {}
for item in student_tuple:
    student_dict[item[0]] = item[1]

for student_id, name in student_dict.items():
    print(f"{student_id} : {name}")
