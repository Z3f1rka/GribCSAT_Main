"""create visits

Revision ID: fffda82735b8
Revises: 
Create Date: 2025-01-25 18:55:30.227058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fffda82735b8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shops',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shops_id'), 'shops', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('reg_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('hashes',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('hash', sa.String(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hashes_id'), 'hashes', ['id'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('article', sa.String(), nullable=False),
    sa.Column('file', sa.String(), nullable=False),
    sa.Column('shop_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_table('shop_comments',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user', sa.BigInteger(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('rating', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('shop', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['shop'], ['shops.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shop_comments_id'), 'shop_comments', ['id'], unique=False)
    op.create_table('visits',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('visited_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_visits_id'), 'visits', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_visits_id'), table_name='visits')
    op.drop_table('visits')
    op.drop_index(op.f('ix_shop_comments_id'), table_name='shop_comments')
    op.drop_table('shop_comments')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_hashes_id'), table_name='hashes')
    op.drop_table('hashes')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_shops_id'), table_name='shops')
    op.drop_table('shops')
    # ### end Alembic commands ###
