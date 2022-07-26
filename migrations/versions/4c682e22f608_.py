"""empty message

Revision ID: 4c682e22f608
Revises: 
Create Date: 2022-07-26 15:46:48.597080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c682e22f608'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('name', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'name', 'category', ['category_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'name', type_='foreignkey')
    op.drop_column('name', 'category_id')
    # ### end Alembic commands ###
