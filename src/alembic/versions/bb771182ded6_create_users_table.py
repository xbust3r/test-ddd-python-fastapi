"""create users table

Revision ID: bb771182ded6
Revises: 
Create Date: 2023-06-06 20:38:35.440619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb771182ded6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', sa.String(36), server_default=sa.text("(UUID())"), unique=True, nullable=False),
        sa.Column('password', sa.String(128), nullable=False),
        sa.Column('name', sa.String(128), unique=True, nullable=False),
        sa.Column('email', sa.String(128), unique=True, nullable=False),
        sa.Column('status', sa.Boolean, nullable=False, default=False),
        sa.Column('active_token', sa.String(length=256), nullable=False),
        sa.Column('auth_token', sa.String(length=256), nullable=True),
        sa.Column('refresh_token', sa.String(length=256), nullable=True),
        sa.Column('last_login', sa.DateTime(), nullable=True),
        sa.Column('phone_number', sa.String(length=20), nullable=True),
        sa.Column('date_of_birth', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        
    )


def downgrade() -> None:
    op.drop_table('users')
