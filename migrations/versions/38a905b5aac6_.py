"""empty message

Revision ID: 38a905b5aac6
Revises: d2bfffef4c08
Create Date: 2020-04-08 15:51:02.562811

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '38a905b5aac6'
down_revision = 'd2bfffef4c08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('posts_ibfk_2', 'posts', type_='foreignkey')
    op.drop_column('posts', 'c_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('c_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('posts_ibfk_2', 'posts', 'categorys', ['c_id'], ['id'])
    # ### end Alembic commands ###
