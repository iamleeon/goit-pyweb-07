from sqlalchemy.sql import func, desc

from connect import session
from models import Group, Student, Teacher, Subject, Mark


def select_1():
    """Find 5 students with the highest average mark from all the subjects"""
    query = session.query(
        Student.student_name, func.round(func.avg(Mark.mark_value), 0).label("average_mark"))\
        .select_from(Student).join(Mark).group_by(Student.id, Student.student_name).order_by(desc("average_mark"))\
        .limit(5).all()
    return query


def select_2():
    """Find a student with the highest average mark from a specific subject"""
    query = session.query(
        Student.student_name, func.round(func.avg(Mark.mark_value), 0).label("average_mark"), Subject.subject_name)\
        .select_from(Student).join(Mark).join(Subject).where(Mark.subject_id_fn == 1)\
        .group_by(Student.id, Student.student_name).order_by(desc("average_mark")).limit(1).all()
    return query


def select_3():
    """Find group average mark from a specific subject"""
    query = session.query(
        Group.group_name, Subject.subject_name, func.round(func.avg(Mark.mark_value), 0).label("average_mark"))\
        .select_from(Group).join(Student).join(Mark).join(Subject).where(Subject.id == 1).group_by(Group.group_name)\
        .all()
    return query


def select_4():
    """Find the average mark across all marks"""
    query = session.query(
        func.round(func.avg(Mark.mark_value), 0).label("average_mark")).select_from(Mark).all()
    return query


def select_5():
    """Find what subjects a certain teacher teaches"""
    query = session.query(
        Subject.subject_name, Teacher.teacher_name).select_from(Subject).join(Teacher).where(Teacher.id == 1).all()
    return query


def select_6():
    """Find the list of students from a group"""
    query = session.query(
        Student.student_name, Group.group_name).select_from(Student).join(Group).where(Group.id == 1)\
        .order_by(Student.student_name).all()
    return query


def select_7():
    """Find marks of a certain subject in a group"""
    query = session.query(
        Student.student_name, Group.group_name, Mark.mark_value, Subject.subject_name).select_from(Mark)\
        .join(Student).join(Group).join(Subject).where(Subject.id == 1).all()
    return query


def select_8():
    """ Find an average mark a teacher gives for their subjects"""
    query = session.query(
        Teacher.teacher_name, Subject.subject_name, func.round(func.avg(Mark.mark_value), 0).label("average_mark"))\
        .select_from(Teacher).join(Subject).join(Mark).where(Teacher.id == 1)\
        .group_by(Teacher.teacher_name, Subject.subject_name).all()
    return query


def select_9():
    """Find subjects that a student attends"""
    query = session.query(
        Student.student_name, Subject.subject_name).select_from(Student).join(Mark).join(Subject)\
        .where(Student.id == 1).group_by(Subject.subject_name).all()
    return query


def select_10():
    """Find a list of subjects that a teacher teaches a student"""
    query = session.query(
        Student.student_name, Subject.subject_name, Teacher.teacher_name).select_from(Subject).join(Teacher)\
        .join(Mark).join(Student).where(Teacher.id == 1).where(Student.id == 1)\
        .group_by(Student.student_name, Subject.subject_name, Teacher.teacher_name).all()
    return query


if __name__ == "__main__":
    print(select_1())
    print(select_2())
    print(select_3())
    print(select_4())
    print(select_5())
    print(select_6())
    print(select_7())
    print(select_8())
    print(select_9())
    print(select_10())
