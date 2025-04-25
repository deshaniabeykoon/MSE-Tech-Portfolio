import numpy as np

scores = np.array([[78, 85, 90],
                   [88, 79, 92],
                   [84, 76, 88],
                   [90, 93, 94],
                   [75, 80, 70]])

def print_seperator_line():
    print("\n--------------------------------------------------")

def display_student_scores(scores):
    print("|--------------------------|")
    print(f"| Student ID | S1, S2, S3  |")
    print("|--------------------------|")
    
    # Using enumerate and unpacking
    for i, (s1, s2, s3) in enumerate(scores, start=1):
        print(f"| Student {i}  | {s1}, {s2}, {s3}  |")
    print("|--------------------------|")
    
    print_seperator_line()


def print_student_averages(scores):
    average_scores = np.mean(scores, axis=1)

    # Method 1: In an array
    print("A1: Average scores for each student:", average_scores, '\n')

    # Method 2: Against each student
    print("A2: Average scores for each student")
    for i, avg in enumerate(average_scores, start=1):
        print(f"Student {i} : Average: {avg:.2f}")

    # Method 3: Scores with average
    print("\nScores and Average scores for each student:")
    print("|-----------------------------------|")
    print(f"| Student ID | S1, S2, S3 | Average |")
    print("|-----------------------------------|")
    for i, (row, avg) in enumerate(zip(scores, average_scores), start=1):
        #print(f"Student {i} : {', '.join(map(str, row))} | Average: {avg:.2f}")
        print(f"| Student {i}  | {', '.join(map(str, row))} |  {avg:.2f}  |")
    print("|-----------------------------------|")

    print_seperator_line()


def print_subject_averages(scores):
    average_scores_subjects = np.mean(scores, axis=0)

    # Method 1: In an array
    print("A1: Average scores for each subject:", average_scores_subjects, '\n')

    # Method 2: Against each subject
    print("A2: Average scores for each subject")
    for i, avg in enumerate(average_scores_subjects, start=1):
        print(f"Subject {i} : Average: {avg:.2f}")

    print("\n|----------------------|")
    print(f"| Subject ID | Average |")
    print("|----------------------|")
    for i, avg in enumerate(average_scores_subjects, start=1):
        print(f"| Subject {i}  |  {avg:.2f}  |")
    print("|----------------------|")

    print_seperator_line()

def print_student_averages_totals(scores, option=None):    
    average_scores = np.mean(scores, axis=1)
    total_scores = np.sum(scores, axis=1)
    top_student_index = np.argmax(total_scores)

    print("Scores, Average scores and Totals for each student")
    print("|-------------------------------------------------|")
    print(f"| Student ID | S1, S2, S3 | Average | Total Score |")
    print("|-------------------------------------------------|")
    for i, (row, avg, tot) in enumerate(zip(scores, average_scores, total_scores), start=1):
        print(f"|  Student {i} | {', '.join(map(str, row))} |  {avg:.2f}  |   {tot}       |")
    print("|-------------------------------------------------|")

    if option == "top":
        print(f"\nStudent with the highest total score: Student {top_student_index + 1}")
        print(f"Total score: {total_scores[top_student_index]}")
        
    print_seperator_line()

def add_bonus_to_third_subject(scores, subjectid, bonus_points):
    # Create a copy to avoid modifying the original array
    updated_scores = scores.copy()
    
    # Add bonus points to the third subject
    updated_scores[:, subjectid] += bonus_points

    print("|-------------------------|")
    print(f"| Student ID | S1, S2, S3 |")
    print("|-------------------------|")
    for i, row in enumerate(updated_scores, start=1):
        print(f"| Student {i}  | {', '.join(map(str, row))} |")
    print("|-------------------------|")
    
    print_seperator_line()
    return updated_scores

# Display the scores for each student in a formatted way
print("Scores of students in different subjects:")
display_student_scores(scores)

# Q1: Calculate and print the average score for each student.
print("Q1: Calculate and print the average score for each student\n")
print_student_averages(scores)

# Q2: Calculate and print the average score for each subject.
print("Q2: Calculate and print the average score for each subject\n")
print_subject_averages(scores)

# Q3: Identify the student (row index) with the highest total score
print("Q3: Identify the student (row index) with the highest total score\n")
print_student_averages_totals(scores,"top")

# 6. Add 5 bonus points to the third subject
print("Q4: Updated Scores after Adding 5 Bonus Points to Third Subject:")
new_scores = add_bonus_to_third_subject(scores,2,5)

print("Q5: Average and total score for each student after Adding 5 Bonus Points to Third Subject")
print_student_averages_totals(new_scores)
