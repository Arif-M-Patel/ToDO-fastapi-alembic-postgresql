"""tasks are added to table

Revision ID: 37a0d1838bb7
Revises: 968ede56ba65
Create Date: 2024-02-16 00:12:55.568174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37a0d1838bb7'
down_revision: Union[str, None] = '968ede56ba65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # initial data
    op.execute("""
        INSERT INTO todos (title, description, completed) 
        VALUES ('task 1', 'this is first task', false), 
               ('task 2', 'this is second task', false)
    """)

def downgrade():
    # Delete inserted data
    op.execute("""
        DELETE FROM todos WHERE id IN (1, 2)
    """)
