#!/usr/bin/python3
"""" This module contains the declaration of states model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from relationship_city import Base


class State(Base):
    """ State model class definition """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all, delete', backref='state')
