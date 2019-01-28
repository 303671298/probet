"""Add table dj_pingbobetresultbill

Revision ID: 5866939ed5d0
Revises: 181f069534f7
Create Date: 2018-08-01 23:26:04.983746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5866939ed5d0'
down_revision = '181f069534f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dj_onlinebill',
    sa.Column('groupId', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('onlineCount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('groupId'),
    mysql_charset='utf8mb4'
    )
    op.create_table('dj_pingbobetbill',
    sa.Column('wagerId', sa.Integer(), nullable=False),
    sa.Column('sport', sa.String(length=45), nullable=True),
    sa.Column('league', sa.String(length=45), nullable=True),
    sa.Column('eventName', sa.String(length=45), nullable=True),
    sa.Column('homeTeam', sa.String(length=45), nullable=True),
    sa.Column('awayTeam', sa.String(length=45), nullable=True),
    sa.Column('selection', sa.String(length=45), nullable=True),
    sa.Column('oddsFormat', sa.Integer(), nullable=True),
    sa.Column('odds', sa.Float(), nullable=True),
    sa.Column('stake', sa.Float(), nullable=True),
    sa.Column('betType', sa.SmallInteger(), nullable=True),
    sa.Column('eventDateFm', sa.Integer(), nullable=True),
    sa.Column('result', sa.String(length=32), nullable=True),
    sa.Column('status', sa.String(length=32), nullable=True),
    sa.Column('toWin', sa.String(length=32), nullable=True),
    sa.Column('toRisk', sa.String(length=32), nullable=True),
    sa.Column('winLoss', sa.Float(), nullable=True),
    sa.Column('currencyCode', sa.String(length=32), nullable=True),
    sa.Column('userCode', sa.String(length=45), nullable=True),
    sa.Column('loginId', sa.String(length=45), nullable=True),
    sa.Column('product', sa.String(length=32), nullable=True),
    sa.Column('wagerDateFm', sa.Integer(), nullable=True),
    sa.Column('agentId', sa.String(length=32), nullable=True),
    sa.Column('settleDateFm', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('wagerId'),
    mysql_charset='utf8mb4'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dj_pingbobetbill')
    op.drop_table('dj_onlinebill')
    # ### end Alembic commands ###
