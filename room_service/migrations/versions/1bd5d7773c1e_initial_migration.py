"""Initial migration

Revision ID: 1bd5d7773c1e
Revises: 514fe804dbe7
Create Date: 2024-12-30 17:35:58.186935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1bd5d7773c1e'
down_revision = '514fe804dbe7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('image_data', sa.LargeBinary(), nullable=False),
    sa.Column('image_name', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('rooms', schema=None) as batch_op:
        batch_op.drop_column('owner_id')
        batch_op.drop_column('images')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rooms', schema=None) as batch_op:
        batch_op.add_column(sa.Column('images', mysql.TEXT(collation='utf8mb4_unicode_ci'), nullable=True))
        batch_op.add_column(sa.Column('owner_id', mysql.INTEGER(), autoincrement=False, nullable=False))

    op.drop_table('images')
    # ### end Alembic commands ###
