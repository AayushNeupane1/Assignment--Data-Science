# 3. Create a dictionary of students and marks; print highest.

student_marks = {

    "Aayush":85,
    "Aastha":90,
    "Smriti":78,
    "Rohan":9
}

print("Student with highest marks:")

for keys in student_marks:
    if student_marks[keys] == max(student_marks.values()):
        print(keys, ":", student_marks[keys])