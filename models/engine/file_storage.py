#!/usr/bin/python3
""" create file storage class """
from models.user import User
import json

class Storage:
    """ file storage class """
    __filepath = "chepr_file.json"
    __objects = {}
    clss = {'user': 'User'}
    def __init__(self):
        """ init storage class """
        
    
    def new(self, obj):
        """ add new object """
        Storage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ save object to file"""
        list_of_obj_attrib = {}
        with open(Storage.__filepath, "w") as file:
            for key, value in Storage.__objects.items():
                list_of_obj_attrib[key] = (value.__dict__)

            json.dump(list_of_obj_attrib, file)

    def all(self):
        """ show all objects in storage """
        return Storage.__objects
    
    def reload(self):
        """ reload objects from file """
        with open(Storage.__filepath, "r") as f:
            dict_obj_attribs = json.load(f)
            for obj in dict_obj_attribs.values():
                cl_name = obj["__class__"]
                obj.pop("__class__")
                self.new(eval(cl_name)(**obj))
                # id_lst = obj["id"].split(".")
                # id = id_lst[1]
                # Storage.__objects[obj["id"]] = obj
