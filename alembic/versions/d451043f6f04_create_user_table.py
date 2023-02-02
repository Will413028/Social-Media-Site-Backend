"""create user table

Revision ID: d451043f6f04
Revises: 
Create Date: 2023-01-30 16:31:10.789768

"""
from alembic import op
import sqlalchemy as sa
from utils.hash import Hash


# revision identifiers, used by Alembic.
revision = 'd451043f6f04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    user = op.create_table('user',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String(32), nullable=True),
    sa.Column('email', sa.String(64), nullable=True),
    sa.Column('password', sa.String(255), nullable=True)
    )

    op.bulk_insert(user,
    [
        {'id':1, 'username':'user1', 'email':'user1@test.com', 'password':Hash.bcrypt('12345678')},
        {'id':2, 'username':'user2', 'email':'user2@test.com', 'password':Hash.bcrypt('12345678')},
        {'id':3, 'username':'user3', 'email':'user3@test.com', 'password':Hash.bcrypt('12345678')},
        {'id':4, 'username':'user4', 'email':'user4@test.com', 'password':Hash.bcrypt('12345678')},
        {'id':5, 'username':'user5', 'email':'user5@test.com', 'password':Hash.bcrypt('12345678')}
    ]
)

def downgrade() -> None:
    op.drop_table('user')
