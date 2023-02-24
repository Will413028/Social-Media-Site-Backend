"""create like table

Revision ID: 7809a737c0d7
Revises: 7e03c61af973
Create Date: 2023-02-16 17:08:15.841498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7809a737c0d7'
down_revision = '7e03c61af973'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('like',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('user_id', sa.Integer, nullable=False),
                    sa.Column('post_id', sa.Integer, nullable=True),
                    sa.Column('comment_id', sa.Integer, nullable=True),
                    sa.Column('timestamp', sa.DateTime, nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
                    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], )
                    )


def downgrade() -> None:
    op.drop_table('like')
