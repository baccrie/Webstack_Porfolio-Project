"""Added new column to post table and added new table called activity that tracks the activities of all user

Revision ID: 086a1d570852
Revises: 347c8828a79f
Create Date: 2023-06-29 10:19:01.614229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '086a1d570852'
down_revision = '347c8828a79f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], name=op.f('fk_activity_admin_id_admin')),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name=op.f('fk_activity_customer_id_customer')),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendor.id'], name=op.f('fk_activity_vendor_id_vendor')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_activity'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('activity')
    # ### end Alembic commands ###