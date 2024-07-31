from sqlalchemy import select
from sqlalchemy.sql import func

from connect import session
from models import Group, Student, Teacher, Subject, Mark


def select_1():
    query = session.execute(
        select(Student.student_name, func.round(func.avg(Mark.mark_value), 0).label("average_mark"))
        .join(Mark)
        .group_by(Student.id, Student.student_name)
        .order_by(func.round(func.avg(Mark.mark_value), 0).desc())
        .limit(5)
    ).mappings().all()

    print(query)


def select_2():
    query = session.execute(
        select(Student.student_name, func.round(func.avg(Mark.mark_value), 0).lable("average_mark"),
               Subject.subject_name)
        .join(Mark)
        .join(Subject)
    )


def select_3():
    pass


def select_4():
    pass


def select_5():
    pass


def select_6():
    pass


def select_7():
    pass


def select_8():
    pass


def select_9():
    pass


def select_10():
    pass


if __name__ == "__main__":
    select_1()
