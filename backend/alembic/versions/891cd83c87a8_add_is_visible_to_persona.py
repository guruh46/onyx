"""Add is_visible to Persona

Revision ID: 891cd83c87a8
Revises: b156fa702355
Create Date: 2023-12-21 11:55:54.132279

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "891cd83c87a8"
down_revision = "b156fa702355"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "persona",
        sa.Column("is_visible", sa.Boolean(), nullable=True),
    )
    op.execute("UPDATE persona SET is_visible = true")
    op.alter_column("persona", "is_visible", nullable=False)

    op.add_column(
        "persona",
        sa.Column("display_priority", sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("persona", "is_visible")
    op.drop_column("persona", "display_priority")
