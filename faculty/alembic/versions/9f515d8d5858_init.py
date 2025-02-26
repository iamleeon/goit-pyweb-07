"""Init

Revision ID: 9f515d8d5858
Revises: 
Create Date: 2024-07-30 19:56:37.498584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f515d8d5858'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('group_name')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('teacher_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('teacher_name')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_name', sa.String(length=255), nullable=False),
    sa.Column('group_id_fn', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id_fn'], ['groups.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_name')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subject_name', sa.String(length=255), nullable=False),
    sa.Column('teacher_id_fn', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id_fn'], ['teachers.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('subject_name')
    )
    op.create_table('marks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mark_value', sa.Integer(), nullable=False),
    sa.Column('mark_date', sa.DateTime(), nullable=False),
    sa.Column('subject_id_fn', sa.Integer(), nullable=True),
    sa.Column('student_id_fn', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id_fn'], ['students.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['subject_id_fn'], ['subjects.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marks')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('teachers')
    op.drop_table('groups')
    # ### end Alembic commands ###
