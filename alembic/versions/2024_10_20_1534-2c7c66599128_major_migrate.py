"""Major migrate

Revision ID: 2c7c66599128
Revises: 
Create Date: 2024-10-20 15:34:55.817708

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2c7c66599128"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "chats",
        sa.Column("title", sa.String(length=128), nullable=False),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("is_group", sa.Boolean(), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_chats")),
    )
    op.create_table(
        "users",
        sa.Column("first_name", sa.String(length=32), nullable=False),
        sa.Column("second_name", sa.String(length=32), nullable=False),
        sa.Column("nickname", sa.String(length=32), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("nickname", name=op.f("uq_users_nickname")),
    )
    op.create_table(
        "message",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("chat_id", sa.Integer(), nullable=False),
        sa.Column("content", sa.String(length=255), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["chat_id"], ["chats.id"], name=op.f("fk_message_chat_id_chats")
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_message_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_message")),
    )
    op.create_table(
        "users_chats",
        sa.Column("chat_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["chat_id"],
            ["chats.id"],
            name=op.f("fk_users_chats_chat_id_chats"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_users_chats_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users_chats")),
    )
    op.execute("INSERT INTO users (first_name, second_name, nickname, hashed_password) VALUES ('Арсений', 'Глушков', 'ars', '$pbkdf2-sha256$29000$0Zqzdq71nnPu/d/bew.B0A$svMz2P9Me3u7H7ApWseyKnsbk5VOtwoYgadPa99TuiQ'),('Петр', 'Петров', 'pit', '$pbkdf2-sha256$29000$0BqDsLbWWitlbC2FUKoV4g$VEhxa/rbC8ydq5VnvvVWn8wmFwVfYIBIByNtTPcG/10'),('Иван', 'Иванов', 'ivan', '$pbkdf2-sha256$29000$QShFSMl5r/Wec651jlGqNQ$.gYApFVaT3xyIZv/41ay4Ker/9KJIED4.HRxx30ACtk')")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_chats")
    op.drop_table("message")
    op.drop_table("users")
    op.drop_table("chats")
    # ### end Alembic commands ###
