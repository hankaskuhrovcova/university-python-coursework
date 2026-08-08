#!/usr/bin/env python3

import ast


class Student:
    id_counter = 1

    def __init__(self, name, exam, coursework):
        self.id = Student.id_counter
        Student.id_counter += 1
        self.name = name
        self.exam = exam
        self.coursework = coursework

    def get_average(self):
        return (
            self.exam + self.coursework
        ) / 2

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Average: {self.get_average()}"
        )


class Module:
    def __init__(self, title, students):
        self.title = title
        self.students = students

    def get_class_average(self):
        average = 0

        for student in self.students:
            average += student.get_average()

        return average / len(self.students)

    def get_students_count(self):
        return len(self.students)

    def get_lowest_student(self):
        lowest = self.students[0]

        for student in self.students[1:]:
            if (
                student.get_average()
                < lowest.get_average()
            ):
                lowest = student

        return lowest

    def get_highest_student(self):
        highest = self.students[0]

        for student in self.students[1:]:
            if (
                student.get_average()
                > highest.get_average()
            ):
                highest = student

        return highest

    def __str__(self):
        return (
            f"Module: {self.title}, "
            f"Has: {self.get_students_count()}, "
            f"Average Mark is: "
            f"{self.get_class_average()}, "
            f"The lowest mark is: "
            f"{self.get_lowest_student()}, "
            f"The highest mark is: "
            f"{self.get_highest_student()}"
        )


module_title = "CSC1035 Programming III"

student_data = [
    ["Mary", "Delaney", 67, 56],
    ["John", "Water", 54, 36],
    ["Ali", "Wall", 47, 96]
]

students = []

for record in student_data:
    name = record[0] + " " + record[1]

    student = Student(
        name,
        record[2],
        record[3]
    )

    students.append(student)

    print(student)

module = Module(module_title, students)

print(module)
