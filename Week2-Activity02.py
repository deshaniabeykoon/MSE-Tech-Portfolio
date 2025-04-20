import numpy as np

scores = np.array([[78, 85, 90],
                   [88, 79, 92],
                   [84, 76, 88],
                   [90, 93, 94],
                   [75, 80, 70]])

# Display the scores for each student in a formatted way
print("Scores of students in different subjects:")

print(f"Student ID : S1, S2, S3")
# Using enumerate and Unpacking
for i, (s1, s2, s3) in enumerate(scores, start=1):
    print(f"Student {i}  : {s1}, {s2}, {s3}")

print("--------------------------------------------------")

# Q1: Calculate and print the average score for each student.
# Average score for each student (row-wise)
average_scores = np.mean(scores, axis=1)
print("Q1: Calculate and print the average score for each student\n")

# Method 1: In an array
print("A1: Average scores for each student:", average_scores, '\n')

# Method 2: Against each student
print("A2: Average scores for each student")
for i, avg in enumerate(average_scores, start=1):
    print(f"Student {i} Average: {avg:.2f}")

print("\nScores and Average scores for each student")
for i, (row, avg) in enumerate(zip(scores, average_scores), start=1):
    print(f"Student {i} : {', '.join(map(str, row))} | Average: {avg:.2f}")

print("--------------------------------------------------")

# Q2: Calculate and print the average score for each subject.
print("Q2: Calculate and print the average score for each subject\n")
average_scores_subjects = np.mean(scores, axis=0)

# Method 1: In an array
print("A1: Average scores for each subject:", average_scores_subjects)

# Method 2: Against each subject
print("A2: Average scores for each subject")
for i, avg in enumerate(average_scores_subjects, start=1):
    print(f"Subject {i} Average: {avg:.2f}")

print("--------------------------------------------------")

# Q3: Identify the student (row index) with the highest total score
print("Q3: Identify the student (row index) with the highest total score\n")
total_scores = np.sum(scores, axis=1)
top_student_index = np.argmax(total_scores)

print("Scores, Average scores and Totals for each student")
for i, (row, avg, tot) in enumerate(zip(scores, average_scores, total_scores), start=1):
    print(f"Student {i} : {', '.join(map(str, row))} | Average: {avg:.2f} | Total Score: {tot}")

print(f"\nStudent with the highest total score: Student {top_student_index + 1}")
print(f"Total score: {total_scores[top_student_index]}")

print("--------------------------------------------------")

# 6. Add 5 bonus points to the third subject
scores[:, 2] += 5
print("\nUpdated Scores after Adding 5 Bonus Points to Third Subject:")
for i, row in enumerate(scores, start=1):
    print(f"Student {i} : {', '.join(map(str, row))}")
