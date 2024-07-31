from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(255), unique=True, nullable=False)

    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(255), unique=True, nullable=False)
    group_id_fn = Column(Integer, ForeignKey('groups.id', ondelete="SET NULL", onupdate="CASCADE"))

    group = relationship("Group", back_populates="students")
    marks = relationship("Mark", back_populates="student")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(255), unique=True, nullable=False)

    subjects = relationship("Subject", back_populates="teacher")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(255), unique=True, nullable=False)
    teacher_id_fn = Column(Integer, ForeignKey('teachers.id', ondelete="SET NULL", onupdate="CASCADE"))

    teacher = relationship("Teacher", back_populates="subjects")
    marks = relationship("Mark", back_populates="subject")


class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    mark_value = Column(Integer, nullable=False)
    mark_date = Column(DateTime, nullable=False)
    subject_id_fn = Column(Integer, ForeignKey('subjects.id', ondelete="SET NULL", onupdate="CASCADE"))
    student_id_fn = Column(Integer, ForeignKey('students.id', ondelete="SET NULL", onupdate="CASCADE"))

    subject = relationship("Subject", back_populates="marks")
    student = relationship("Student", back_populates="marks")
