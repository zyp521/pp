"""empty message

Revision ID: 5093a5048f46
Revises: b85a680ff053
Create Date: 2020-09-30 14:48:29.130615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5093a5048f46'
down_revision = 'b85a680ff053'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendance', sa.Column('adate', sa.Float(), nullable=True))
    op.add_column('attendance', sa.Column('astauts', sa.String(length=32), nullable=True))
    op.add_column('attendance', sa.Column('atype', sa.String(length=32), nullable=True))
    op.add_column('attendance', sa.Column('end_time', sa.Date(), nullable=True))
    op.add_column('attendance', sa.Column('examine', sa.String(length=32), nullable=True))
    op.add_column('attendance', sa.Column('person_id', sa.Integer(), nullable=True))
    op.add_column('attendance', sa.Column('reason', sa.Text(), nullable=True))
    op.add_column('attendance', sa.Column('start_time', sa.Date(), nullable=True))
    op.create_foreign_key(None, 'attendance', 'person', ['person_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'attendance', type_='foreignkey')
    op.drop_column('attendance', 'start_time')
    op.drop_column('attendance', 'reason')
    op.drop_column('attendance', 'person_id')
    op.drop_column('attendance', 'examine')
    op.drop_column('attendance', 'end_time')
    op.drop_column('attendance', 'atype')
    op.drop_column('attendance', 'astauts')
    op.drop_column('attendance', 'adate')
    # ### end Alembic commands ###
