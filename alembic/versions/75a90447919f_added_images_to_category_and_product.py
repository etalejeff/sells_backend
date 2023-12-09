"""added images to category and product

Revision ID: 75a90447919f
Revises: 5c528c8065bb
Create Date: 2023-12-09 23:16:03.177315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75a90447919f'
down_revision: Union[str, None] = '5c528c8065bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('image', sa.String(), nullable=True))
    op.create_index(op.f('ix_categories_image'), 'categories', ['image'], unique=False)
    op.add_column('products', sa.Column('image', sa.String(), nullable=True))
    op.create_index(op.f('ix_products_image'), 'products', ['image'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_image'), table_name='products')
    op.drop_column('products', 'image')
    op.drop_index(op.f('ix_categories_image'), table_name='categories')
    op.drop_column('categories', 'image')
    # ### end Alembic commands ###
