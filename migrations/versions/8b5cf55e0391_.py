"""empty message

Revision ID: 8b5cf55e0391
Revises: 14cc596a5499
Create Date: 2016-09-26 19:54:53.302633

"""

# revision identifiers, used by Alembic.
revision = '8b5cf55e0391'
down_revision = '14cc596a5499'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('runs',
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=120), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.Column('workout_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('runs')
    ### end Alembic commands ###