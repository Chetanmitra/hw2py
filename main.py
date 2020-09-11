# Author: Chetan Mitra czm5805@psu.edu

def getGradepoint(grade):
  if grade=="A":
    return 4.0
  elif grade =="A-":
    return 3.67
  elif grade=="B+":
    return 3.33
  elif grade=="B":
    return 3.00
  elif grade=="B-":
    return 2.67
  elif grade=="C+":
    return 2.33
  elif grade=="C":
    return 2.0
  elif grade=="D":
    return 1.0
  else:
    return 0.0

c1grade = input("Enter your course 1 letter grade: ")
gradepoint1 = getGradepoint(c1grade)
credit1 = float(input("Enter your course 1 credit: "))
print(f"Grade point for course 1 is: {gradepoint1}")

c2grade = input("Enter your course 2 letter grade: ")
gradepoint2 = getGradepoint(c2grade)
credit2 = float(input("Enter your course 2 credit: "))
print(f"Grade point for course 2 is: {gradepoint2}")

c3grade = input("Enter your course 3 letter grade: ")
gradepoint3 = getGradepoint(c3grade)
credit3 = float(input("Enter your course 3 credit: "))
print(f"Grade point for course 3 is: {gradepoint3}")


GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 
print(f"Your GPA is: {GPA}")