"""create comment table

Revision ID: 7e03c61af973
Revises: e702a3ecf8c3
Create Date: 2023-02-06 11:41:15.335538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e03c61af973'
down_revision = 'e702a3ecf8c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('comment',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('text', sa.String(255), nullable=True),
                    sa.Column('timestamp', sa.DateTime, nullable=True),
                    sa.Column('post_id', sa.Integer, nullable=True),
                    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
                    sa.Column('user_id', sa.Integer, nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
                    )


def downgrade() -> None:
    op.drop_table('comment')
