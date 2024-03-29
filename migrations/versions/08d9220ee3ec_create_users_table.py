"""Create users table

Revision ID: 08d9220ee3ec
Revises: 
Create Date: 2022-05-27 17:16:06.613693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08d9220ee3ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('nome', sa.String(length=120), nullable=True),
    sa.Column('cidade', sa.String(length=120), nullable=True),
    sa.Column('estado', sa.String(length=120), nullable=True),
    sa.Column('genero', sa.String(length=32), nullable=True),
    sa.Column('tipo_sanguineo', sa.String(length=32), nullable=True),
    sa.Column('senha_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
