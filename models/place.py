#!/usr/bin/python3
""" Place Module for HBNB project """
from re import S
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ColumnDefault, Table
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), nullable=False),
                      Column('amenity_id', String(60,),
                             ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, ColumnDefault(0), nullable=False)
    number_bathrooms = Column(Integer, ColumnDefault(0), nullable=False)
    max_guest = Column(Integer,  ColumnDefault(0), nullable=False)
    price_by_night = Column(Integer,  ColumnDefault(0), nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place")
    amenity_ids = []
    amenities = relationship("Amenity", secondary=place_amenity,
                             back_populates="place_amenities")
