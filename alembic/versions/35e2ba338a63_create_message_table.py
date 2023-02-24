"""create message table

Revision ID: 35e2ba338a63
Revises: a2a2062637c0
Create Date: 2023-02-16 18:38:18.388026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35e2ba338a63'
down_revision = 'a2a2062637c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('message',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('message', sa.String(255), nullable=True),
                    sa.Column('sender_id', sa.Integer, nullable=False),
                    sa.Column('recipient_id', sa.Integer, nullable=False),
                    sa.Column('status', sa.Boolean, nullable=True),
                    sa.Column('timestamp', sa.DateTime, nullable=False),
                    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], )
                    )


def downgrade() -> None:
    op.drop_table('message')
