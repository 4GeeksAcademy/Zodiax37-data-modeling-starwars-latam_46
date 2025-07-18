"""empty message

Revision ID: c08b0557d24f
Revises: 1063644fddca
Create Date: 2025-05-29 00:35:29.107488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c08b0557d24f'
down_revision = '1063644fddca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['id'], ['favorite.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['favorite.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.drop_constraint('favorite_character_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite_planet_id_fkey', type_='foreignkey')
        batch_op.drop_column('planet_id')
        batch_op.drop_column('character_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('planet_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('favorite_planet_id_fkey', 'planet', ['planet_id'], ['id'])
        batch_op.create_foreign_key('favorite_character_id_fkey', 'character', ['character_id'], ['id'])

    op.drop_table('favorite_planet')
    op.drop_table('favorite_character')
    # ### end Alembic commands ###
