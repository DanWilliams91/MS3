"""empty message

Revision ID: 61328df0aa77
Revises: 447dca615a3b
Create Date: 2022-08-11 11:44:09.767331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61328df0aa77'
down_revision = '447dca615a3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('category_img', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'category_img')
    # ### end Alembic commands ###