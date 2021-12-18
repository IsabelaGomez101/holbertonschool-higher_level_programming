#!/usr/bin/python3
"""
class definition of a City and an instance Base = declarative_base()
"""

import MySQLdb
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State


Base = declarative_base()


class City(Base):
    """
    class City, inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
