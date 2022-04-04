"""add last columns to posts table

Revision ID: 83379f8cc0bf
Revises: 6b675c8b3a8e
Create Date: 2022-04-04 18:05:02.786633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83379f8cc0bf'
down_revision = '6b675c8b3a8e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="True"),
                  op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('Now()'))))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
