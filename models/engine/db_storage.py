#!/usr/bin/python3
"""contains dbstorage class"""

from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """interacts with db"""
    __engine = None
    __session = None

    def __init__(self):
        """creates instance"""

        user = getenv('HBN_MYSQL_USER')
        passwd = getenv('HBN_MYSQL_PWD')
        host = getenv('HBN_MYSQL_HOST')
        db = getenv('HBN_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'. format(user, passwd, host, db),
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the database"""

        n_list = [User, State, City, Amenity, Place, Review]
        n_dict = {}

        if cls is not None:
            result = self.__session.query(type(cls)).all()
        else:
            result = self.__session.query(n_list).all()

        for r in result:
            id = r.__class__.__name__ + '.' + r._id
            n_dict[id] = r
        return(n_dict)
