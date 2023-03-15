#!/usr/bin/python3
""" create promotion class """
from models.base import Base

class Promotion (Base):
    product_service_id = ""
    promotion_start_date = None
    promotion_end_date = None