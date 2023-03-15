#!/usr/bin/python3
""" cleare base class for all other classes """
from datetime import datetime
import uuid

class Base:
    """ base class """
    def __init__(self, *args, **kwargs):
        """ init base class """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.to_dict()

    def to_dict(self):
        """ convert id and dates to string in dict"""
        created = self.created_at.strftime("%m-%d-%Y %H:%M:%S")
        updated =self.updated_at.strftime("%m-%d-%Y %H:%M:%S")
        new_id = str(self.id)
        self.__dict__["id"] = new_id
        self.__dict__["created_at"] = created
        self.__dict__["updated_at"] = updated
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__

# base = Base()
# base.name = "Wonde"
# base.age = "33"

# print(base.to_dict())