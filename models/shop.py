#!/usr/bin/python3
""" create shop class """
from models.base import Base

class Shop(Base):
    """ shop class """
    owner = ""
    name = ""
    type = ""
    product_service = ""
    gps_location = ""
    city = ""
