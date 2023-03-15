#!/usr/bin/python3
""" create product or service class"""
from models.base import Base

class ProductService(Base):
    name = ""
    brand = ""
    quality = ""
    price = ""
    shop = ""