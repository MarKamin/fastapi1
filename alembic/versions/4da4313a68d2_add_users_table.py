"""add users table

Revision ID: 4da4313a68d2
Revises: 6cf9f2ad82af
Create Date: 2022-01-25 00:15:24.879043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da4313a68d2'
down_revision = '6cf9f2ad82af'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
    pass


def downgrade():
    op.drop_table('users')
    pass

