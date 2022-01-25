"""add content column to post table

Revision ID: 6cf9f2ad82af
Revises: ab0e2241bf2d
Create Date: 2022-01-25 00:14:26.217895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cf9f2ad82af'
down_revision = 'ab0e2241bf2d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
