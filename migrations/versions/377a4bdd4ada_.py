"""empty message

Revision ID: 377a4bdd4ada
Revises: 34d41a013f9d
Create Date: 2015-08-19 10:25:01.396786

"""

# revision identifiers, used by Alembic.
revision = '377a4bdd4ada'
down_revision = '34d41a013f9d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'roles', ['role_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    ### end Alembic commands ###
