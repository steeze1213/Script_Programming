student_tuple = [('241101', '강이안', '010-123-1111'), 
                 ('241102', '박동민', '010-123-2222'), 
                 ('241103', '김수정', '010-123-3333')]

def find_student_info(student_id):
    for student in student_tuple:
        if student[0] == student_id:
            return student[1], student[2]
    return None, None

student_id = input("학번을 입력하세요: ")
name, phone_number = find_student_info(student_id)

if name and phone_number:
    print(f"{student_id} 학생은 {name}이며, 전화번호는 {phone_number}입니다.")
else:
    print("해당 학번의 학생이 존재하지 않습니다.")
