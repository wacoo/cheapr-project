#!/usr/bin/python3
""" create shop class """
from models.base import Base

class Shop(Base):
    """ shop class """
    name = ""
    type = ""
    gps_location = ""
    city = ""
