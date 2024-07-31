import faker
from faker.providers import BaseProvider
from datetime import datetime
from random import randint, choice
from connect import session
from models import Group, Student, Teacher, Subject, Mark


STUDENTS_NUMBER = 30
GROUPS_NUMBER = 3
TEACHERS_NUMBER = 5
SUBJECTS_NUMBER = 4


class UniversitySubjectProvider(BaseProvider):
    def university_subject(self):
        faculty_subjects = [
            "Mathematics", "English", "History", "Geography", "Biology",
            "Chemistry", "Physics", "Physical Education", "Art", "Music",
            "Computer Science", "Economics", "Psychology", "Sociology",
            "Political Science", "Literature", "Foreign Languages", "Philosophy",
            "Religious Studies", "Drama"
        ]
        return choice(faculty_subjects)


def generate_fake_data(students_number, groups_number, teachers_number, subjects_number) -> tuple():
    fake_students = []
    fake_groups = []
    fake_teachers = []
    fake_subjects = []

    fake_data = faker.Faker()
    fake_data.add_provider(UniversitySubjectProvider)

    for _ in range(students_number):
        fake_students.append(fake_data.name())

    for _ in range(groups_number):
        fake_groups.append(fake_data.city())

    for _ in range(teachers_number):
        fake_teachers.append(fake_data.name())

    for _ in range(subjects_number):
        fake_subjects.append(fake_data.university_subject())

    return fake_students, fake_groups, fake_teachers, fake_subjects


def prepare_data(students, groups, teachers, subjects) -> tuple():
    for_students = []
    for student in students:
        for_students.append((student, randint(1, GROUPS_NUMBER)))

    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, TEACHERS_NUMBER)))

    for_marks = []
    for month in range(1, 12 + 1):
        mark_date = datetime(2024, randint(1, 6), randint(1, 28)).date()
        for student in range(1, STUDENTS_NUMBER + 1):
            for_marks.append((
                randint(0, 100),
                mark_date,
                randint(1, SUBJECTS_NUMBER),
                student
            ))

    return for_students, for_groups, for_teachers, for_subjects, for_marks


def insert_data_to_db(students, groups, teachers, subjects, marks):
    for group in groups:
        session.add(Group(group_name=group[0]))

    session.commit()

    for student, group_id in students:
        session.add(Student(student_name=student, group_id_fn=group_id))

    session.commit()

    for teacher in teachers:
        session.add(Teacher(teacher_name=teacher[0]))

    session.commit()

    for subject, teacher_id in subjects:
        session.add(Subject(subject_name=subject, teacher_id_fn=teacher_id))

    session.commit()

    for mark_value, mark_date, subject_id, student_id in marks:
        session.add(Mark(mark_value=mark_value, mark_date=mark_date, subject_id_fn=subject_id, student_id_fn=student_id))

    session.commit()


if __name__ == '__main__':
    students, groups, teachers, subjects, marks = prepare_data(*generate_fake_data(
        STUDENTS_NUMBER, GROUPS_NUMBER, TEACHERS_NUMBER, SUBJECTS_NUMBER))
    insert_data_to_db(students, groups, teachers, subjects, marks)