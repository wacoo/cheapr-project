#!/usr/bin/python3
""" create file storage class """
from models.user import User
from models.promotion import Promotion
from models.shop import Shop
from models.product import Product
from models.service import Service
import json

class Storage:
    """ file storage class """
    __filepath = "chepr_file.json"
    __objects = {}
    clss = ['User', 'Product', 'Service', 'Shop', 'Promition']
    def __init__(self):
        """ init storage class """
        
    
    def new(self, obj):
        """ add new object """
        #try: 
        if obj.__dict__["__class__"] == "User":
            for ob in self.all().values():
                if ob.__dict__["__class__"] == "User":
                    if ob.__dict__["username"] == obj.__dict__["username"]:
                        return False
        Storage.__objects[obj.__class__.__name__ + "." + obj.id] = obj        
        self.save()
        return True
        #except Exception as e:
        #    print(e)   

    #             self.get(type, )
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
            try:
                dict_obj_attribs = json.load(f)
                if dict_obj_attribs:
                    for obj in dict_obj_attribs.values():
                        cl_name = obj["__class__"]
                        self.new(eval(cl_name)(**obj)) # same as self.new(User(obj))
            except Exception as e:
                print(e)
    
    def delete(self, obj=None):
        """ remove object from Storage.__objects """
        if obj:
            cname = obj.__class__.__name__ + "." + obj.id
            keys = tuple(Storage.__objects.keys())
            for key in keys:
                if key == cname:
                    Storage.__objects.pop(key)
    

    def get(self, cls, id):
        """ return an object requested """
        lst = []
        if cls in Storage.clss and id:
            ob_id = cls + "." + id            
            for key, val in Storage.__objects.items():
                if key == ob_id:
                    return val
        elif cls in Storage.clss and not id:
            for key, val in Storage.__objects.items():
                if cls == val.__dict__['__class__']:
                    lst.append(val.__dict__['name'])
        return None
    
    def get_by_username(self, uname):
        """ return an object requested """
        lst = []
        if uname:
            for obj in self.all().values():
                if obj.__dict__['__class__'] == "User":
                    if (uname == obj.__dict__['username']):
                        return obj.__dict__
        return None
    
    def getby(self, cls):
        """ return list of same class """
        lst = [];
        if cls in Storage.clss:
            for val in Storage.__objects.values():
                if cls == val.__dict__['__class__']:
                    lst.append(val.__dict__)
            return lst
        else:
            return None

    def count(self, cls=None):
        """ counts the number of objects """
        count = 0
        if not cls:
            for key in Storage.__objects.keys():
                count += 1
        else:
            for val in Storage.__objects.values():
                if cls == val.__class__.__name__:
                    count += 1
        return count
    
    def getpass(self, uname=None):
        """ return password"""
        if uname:
            self.reload()
            for obj in self.all().values():
                if obj.__dict__['__class__'] == 'User':
                    if uname == obj.__dict__["username"]:
                        return obj.__dict__["password"]
            return None

