"""create follower table

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
    op.create_table('follower',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('follower_id', sa.Integer, nullable=False),
                    sa.Column('followee_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['followee_id'], ['user.id'], )
                    )


def downgrade() -> None:
    op.drop_table('follower')
