"""empty message

Revision ID: 03_create_exercise
Revises: 02_create_assessment
Create Date: 2021-05-29 13:31:37.873341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03_create_exercise'
down_revision = '02_create_assessment'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercise')
    # ### end Alembic commands ###
