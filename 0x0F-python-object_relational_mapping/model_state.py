#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Representation of a state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
