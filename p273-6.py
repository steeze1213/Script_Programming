s = "English = 89, Science = 90, Math = 92, History = 80."

total_score = 0
num_scores = 0

subjects_and_scores = s.split(',')

for subject_and_score in subjects_and_scores:
    subject, score = subject_and_score.split('=')
    total_score += float(score.strip())
    num_scores += 1

average_score = total_score / num_scores

print("총점:", int(total_score))
print("평균점수:", average_score)
