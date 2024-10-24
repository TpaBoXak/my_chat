"""remove name from chats

Revision ID: 2340e017936e
Revises: 2c7c66599128
Create Date: 2024-10-21 01:15:02.486392

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2340e017936e"
down_revision: Union[str, None] = "2c7c66599128"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("chats", "name")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chats",
        sa.Column(
            "name", sa.VARCHAR(length=256), autoincrement=False, nullable=False
        ),
    )
    # ### end Alembic commands ###
