"""create post table

Revision ID: e702a3ecf8c3
Revises: d451043f6f04
Create Date: 2023-02-03 11:18:32.875482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e702a3ecf8c3'
down_revision = 'd451043f6f04'
branch_labels = None
depends_on = None


def upgrade() -> None:
    user = op.create_table('post',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('image_url', sa.String(255), nullable=True),
    sa.Column('image_url_type', sa.String(36), nullable=True),
    sa.Column('caption', sa.String(36), nullable=True),
    sa.Column('timestamp', sa.DateTime, nullable=True),
    sa.Column('user_id', sa.Integer, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )


def downgrade() -> None:
    op.drop_table('post')