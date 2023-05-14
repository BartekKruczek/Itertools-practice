import roster
import classroom_organizer


class Students:
    def __init__(self, studentList):
        self.studentsList = studentList

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(roster.student_roster):
            student_status = self.studentsList[self.index]
            self.index += 1
            return student_status
        else:
            raise StopIteration


student_cls = Students(roster.student_roster)
students_iter = iter(student_cls)

# 1: Create an iterator for the student_roster list and print out each student’s information using next().
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))
print(next(students_iter))

# 4. print out the result to see all the possible table combinations of two students
print(classroom_organizer.student_tables)

# 5. Retrieve a list of all 4 combinations of students whose favorite subjects are Math and Science.
# print the final list of combinations
print(classroom_organizer.two_subjects_combo)
