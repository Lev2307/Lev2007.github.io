exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]

summa = 0
for grade in grades:
  sum = summa + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = 5
elif avg >= 80 and avg < 90:
    letter_grade = 4
elif avg > 69 and avg < 80:
    letter_grade = 3
elif avg <= 69 and avg >= 65:
    letter_grade = 2
else:
    letter_grade = 1

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))

if letter_grade is 1:
    print("Student is failing.")
else:
    print("Student is passing.")