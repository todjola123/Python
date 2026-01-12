all_names = []
all_scores = []
all_grades = []

print("--- Student Grade System ---")
print("(Type 'stop' as the name when you are finished)")

while True:
    student_name = input("\nEnter the student's name: ")

    if student_name.lower() == "stop":
        break

    score = float(input("Enter the test score (0-100): "))

    if score >= 90:
        grade = "A"
        status = "Pass"
    elif score >= 80:
        grade = "B"
        status = "Pass"
    elif score >= 70:
        grade = "C"
        status = "Pass"
    elif score >= 50:
        grade = "D"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    all_names.append(student_name)
    all_scores.append(score)
    all_grades.append(grade)

    print(f"Added {student_name} to the list.")

print("\n" + "=" * 20)
print("FINAL RESULTS")
print("=" * 20)

print(f"All Student Names: {all_names}")
print(f"All Student Grades: {all_grades}")

print("\nIndividual Records:")

for i in range(len(all_names)):
    print(f"Student: {all_names[i]} | Grade: {all_grades[i]}")
