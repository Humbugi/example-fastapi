"""add content column to posts table

Revision ID: c95499fee8ae
Revises: ff841e215cc7
Create Date: 2022-04-04 17:19:37.971892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c95499fee8ae'
down_revision = 'ff841e215cc7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
