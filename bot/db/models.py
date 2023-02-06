from sqlalchemy import Column, Integer, BigInteger, Boolean, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Subscriber(Base):
    __tablename__ = 'subscribers'
    user_id = Column(BigInteger, primary_key=True)
    chat_id = Column(BigInteger, nullable=False)
    