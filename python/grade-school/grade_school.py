from collections import defaultdict


class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self):
        grades = list(self.students.keys())
        grades.sort()

        o_names = []
        for g in grades:
            o_names += self.students[g]
        return o_names

    def grade(self, grade_number):
        return self.students[grade_number] if grade_number in self.students else []
