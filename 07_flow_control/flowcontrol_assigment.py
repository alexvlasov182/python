"""
Grades:
A = 90 - 100
B = 80 - 89
C = 70 - 79
D = 60 - 69
D = 0 - 59

- create a variable (grade) holding na integer between 0 and 100
- write if, elif, else statements to print the letter grade
    of the number grade variable
"""
grade: int = 110
if grade >= 90:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")
elif grade >= 60 and grade < 70:
    print("D")
else:
    print("F    ")
