"""empty message

Revision ID: 5e2c32e8ed30
Revises: 
Create Date: 2023-01-16 16:00:11.969645

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e2c32e8ed30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fantasy_premierleague')
    op.drop_table('items_tags')
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    op.create_table('items_tags',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name='items_tags_item_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='items_tags_tag_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='items_tags_pkey')
    )
    op.create_table('fantasy_premierleague',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('firstname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('position', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gametime', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('form', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('bps', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('inserted_dtime', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
