from itertools import combinations, chain
from roster import student_roster


# Import modules above this line
class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        all_students = self.sorted_names[self.index]
        self.index += 1
        if self.index >= 10:
            raise StopIteration
        return all_students

    def _sort_alphabetically(self, students):
        names = []
        for student_info in students:
            name = student_info["name"]
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student["favorite_subject"] == subject:
                selected_students.append((student["name"], subject))
        return selected_students

    def table_seating(self):
        names = []
        for student_info in student_roster:
            name = student_info["name"]
            names.append(name)
            table_list = list(combinations(names, 2))
        return table_list

    def two_subjects_tables(self):
        math = []
        science = []
        for student_info in student_roster:
            fav_subject = student_info["favorite_subject"]
            if fav_subject == "Math":
                math.append(student_info["name"])
            if fav_subject == "Science":
                science.append(student_info["name"])
            two_subjects_list = list(chain(math, science))
            two_subjects_combos = list(combinations(two_subjects_list, 4))
        return two_subjects_combos


student_roll = ClassroomOrganizer()
student_roll_iter = iter(student_roll)
for student in student_roll_iter:
    print(student)

tables = ClassroomOrganizer()
student_tables = tables.table_seating()
print(student_tables)

# Test
two_subjects = ClassroomOrganizer()
two_subjects_combo = two_subjects.two_subjects_tables()
print(two_subjects_combo)
