#!/usr/bin/python3
""" create product or service class"""
from models.base import Base

class Service(Base):
    name = ""
    category = ""
    quality = ""
    price = ""
    provider = ""
    photo = ""