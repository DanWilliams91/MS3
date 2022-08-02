"""empty message

Revision ID: 681b5f06b0cb
Revises: 
Create Date: 2022-08-02 15:21:52.459897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '681b5f06b0cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('name', 'recipe_name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('name', 'recipe_name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)
    # ### end Alembic commands ###