import datetime, time
import sqlalchemy as sa
import sqlalchemy.orm as saorm
import sqlalchemy.ext.declarative
from node.config.server_config import server_config as config



Base = sqlalchemy.ext.declarative.declarative_base()
db_engine = sa.create_engine(config.db.url, echo=config.db.echo, encoding='utf-8', pool_recycle=3600)
Session = saorm.sessionmaker(bind=db_engine)



def get_date():
    return datetime.datetime.now()

def get_timestamp():
    return time.time()


class Transaction(Base):
    __tablename__   = 'transaction'

    tx_hash     = sa.Column(sa.String(256), primary_key=True)
    _from       = sa.Column(sa.String(64), nullable=False)
    to          = sa.Column(sa.String(64), nullable=False)
    sig         = sa.Column(sa.String(256), nullable=False)
    value       = sa.Column(sa.BIGINT, nullable=False)
    nonuce      = sa.Column(sa.Integer, nullable=False)
    timestamp   = sa.Column(sa.Float, nullable=False, default=get_timestamp)
    memo        = sa.Column(sa.String(256), nullable=True)

    def __repr__(self):
        return '<Transaction %d>' % (self.tx_hash)


Base.metadata.create_all(db_engine)
