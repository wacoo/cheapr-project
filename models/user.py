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

# user = User()
# user.username = "wac"
# user.password = "wacNRD"
# user.firstname = "Wondmagegn"
# user.middlename = "Abriham"
# user.lastname = "Chosha"
# user.usertype = "Agent"
# user.active = True
# user.age = 20
# print(user.to_dict())
