"""create user table

Revision ID: d451043f6f04
Revises: 
Create Date: 2023-01-30 16:31:10.789768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd451043f6f04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String(32), nullable=True),
    sa.Column('email', sa.String(64), nullable=True),
    sa.Column('password', sa.String(255), nullable=True)
    )

def downgrade() -> None:
    op.drop_table('user')
