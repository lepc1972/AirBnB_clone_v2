#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm.base import attribute_str
from models.base_model import BaseModel, base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy
from models.city import City
import models


class State(BaseModel, base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")

    @property
    def cities(self):
        """getter of cities instances"""
        return self.cities
