from datetime import datetime

from sqlalchemy import Column, BIGINT, VARCHAR, REAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Proxies(Base):
    __tablename__ = 'proxies'
    id = Column('id', BIGINT(), primary_key=True, autoincrement=True)
    value = Column('value', VARCHAR(length=21), nullable=True, unique=True)
    type_ = Column('type', VARCHAR(length=6), nullable=True)
    response = Column('response', REAL(), nullable=True)
    created_on = Column('created_on', TIMESTAMP(), default=datetime.now)
    updated_on = Column('updated_on', TIMESTAMP(), default=datetime.now, onupdate=datetime.now)

    def __init__(self, value: str, type_: str, response: float):
        self.value = value
        self.type_ = type_
        self.response = response
