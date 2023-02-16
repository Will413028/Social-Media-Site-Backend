"""create following table

Revision ID: a2a2062637c0
Revises: 7809a737c0d7
Create Date: 2023-02-16 17:08:29.281431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2a2062637c0'
down_revision = '7809a737c0d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('following',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, nullable=False),
    sa.Column('follower_id', sa.Integer, nullable=False),
    sa.Column('timestamp', sa.DateTime, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    )

def downgrade() -> None:
    op.drop_table('following')
