#!/usr/bin/python3
""" create user class """
from models.base import Base
class User(Base):
    """ user class """    
    firstname = ""
    middlename = ""
    lastname = ""
    username = ""
    password = ""
    usertype= ""
    active= False
    
