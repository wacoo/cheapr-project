#!/usr/bin/python3
""" create product or service class"""
from models.base import Base

class ProductService(Base):
    name = ""
    brand = ""
    model = ""
    category = ""
    manufature_date = ""
    status = ""
    quality = ""
    price = ""
    shop = ""