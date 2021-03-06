"""empty message

Revision ID: 4d6c87eb4fbf
Revises: de0dc4a55970
Create Date: 2016-05-30 12:30:52.432415

"""

# revision identifiers, used by Alembic.
revision = '4d6c87eb4fbf'
down_revision = 'de0dc4a55970'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cobra_project',
    sa.Column('id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('repo_type', mysql.TINYINT(display_width=2), nullable=False),
    sa.Column('repository', sa.String(length=256), nullable=True),
    sa.Column('branch', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('scan_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cobra_project')
    ### end Alembic commands ###
