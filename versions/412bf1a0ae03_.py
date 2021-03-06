"""empty message

Revision ID: 412bf1a0ae03
Revises: 
Create Date: 2021-06-03 18:21:12.531460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '412bf1a0ae03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_index(op.f('ix_groups_id'), 'groups', ['id'], unique=False)
    op.create_table('sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('link', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sources_id'), 'sources', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('hashed_password', sa.String(length=256), nullable=True),
    sa.Column('robot', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('bind_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('link', sa.String(length=256), nullable=True),
    sa.Column('last_spider', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username', 'source_id')
    )
    op.create_index(op.f('ix_bind_user_id'), 'bind_user', ['id'], unique=False)
    op.create_index(op.f('ix_bind_user_username'), 'bind_user', ['username'], unique=False)
    op.create_table('problems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('problem_id', sa.String(length=128), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('link', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source_id', 'problem_id')
    )
    op.create_index(op.f('ix_problems_id'), 'problems', ['id'], unique=False)
    op.create_index(op.f('ix_problems_problem_id'), 'problems', ['problem_id'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_index(op.f('ix_roles_name'), 'roles', ['name'], unique=False)
    op.create_table('steps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('source', sa.String(length=32), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_steps_id'), 'steps', ['id'], unique=False)
    op.create_table('solutions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('result', sa.Enum('Accepted', 'WrongAnswer', 'TimeLimitExceeded', 'MemoryLimitExceeded', 'RuntimeError', 'OutputLimitExceeded', 'CompileError', 'PresentationError', 'SystemError', 'Unknown', name='resultenum'), nullable=True),
    sa.Column('time_used', sa.Integer(), nullable=True),
    sa.Column('memory_used', sa.Integer(), nullable=True),
    sa.Column('code_len', sa.Integer(), nullable=True),
    sa.Column('language', sa.Enum('C', 'Cpp', 'Python', 'Java', 'Go', 'Rust', 'JavaScript', 'TypeScript', 'CSharp', 'Pascal', 'Fortran', 'Unknown', name='languageenum'), nullable=True),
    sa.Column('submitted_at', sa.DateTime(), nullable=True),
    sa.Column('bind_user_id', sa.Integer(), nullable=True),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bind_user_id'], ['bind_user.id'], ),
    sa.ForeignKeyConstraint(['problem_id'], ['problems.id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_solutions_id'), 'solutions', ['id'], unique=False)
    op.create_index(op.f('ix_solutions_submitted_at'), 'solutions', ['submitted_at'], unique=False)
    op.create_index(op.f('ix_solutions_username'), 'solutions', ['username'], unique=False)
    op.create_index('solution_bind_user_id_problem_id', 'solutions', ['bind_user_id', 'problem_id'], unique=False)
    op.create_table('step_problem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project', sa.String(length=64), nullable=True, comment='专项'),
    sa.Column('topic', sa.String(length=64), nullable=True, comment='专题'),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.Column('step_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problem_id'], ['problems.id'], ),
    sa.ForeignKeyConstraint(['step_id'], ['steps.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_step_problem_id'), 'step_problem', ['id'], unique=False)
    op.create_table('step_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('clazz', sa.String(length=64), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('step_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['step_id'], ['steps.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_step_user_id'), 'step_user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_step_user_id'), table_name='step_user')
    op.drop_table('step_user')
    op.drop_index(op.f('ix_step_problem_id'), table_name='step_problem')
    op.drop_table('step_problem')
    op.drop_index('solution_bind_user_id_problem_id', table_name='solutions')
    op.drop_index(op.f('ix_solutions_username'), table_name='solutions')
    op.drop_index(op.f('ix_solutions_submitted_at'), table_name='solutions')
    op.drop_index(op.f('ix_solutions_id'), table_name='solutions')
    op.drop_table('solutions')
    op.drop_index(op.f('ix_steps_id'), table_name='steps')
    op.drop_table('steps')
    op.drop_index(op.f('ix_roles_name'), table_name='roles')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_problems_problem_id'), table_name='problems')
    op.drop_index(op.f('ix_problems_id'), table_name='problems')
    op.drop_table('problems')
    op.drop_index(op.f('ix_bind_user_username'), table_name='bind_user')
    op.drop_index(op.f('ix_bind_user_id'), table_name='bind_user')
    op.drop_table('bind_user')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_sources_id'), table_name='sources')
    op.drop_table('sources')
    op.drop_index(op.f('ix_groups_id'), table_name='groups')
    op.drop_table('groups')
    # ### end Alembic commands ###
