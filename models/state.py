#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm.base import attribute_str
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy
from models.city import City
import models



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")
