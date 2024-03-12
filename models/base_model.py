#!/usr/bin/python3
"""The base class of the models"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """This is the parent class for all the models"""
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
       
        if kwargs:
           for key, value in kwargs.items():
               if key == "__class__":
                   continue
               elif key == "created_at" or key == "updated_at":
                   setattr(self, key, datetime.strptime(value,time_format))
               else:
                   setattr(self, key, value)

        models.storage.new(self)


    def save(self):
        """ 
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        """
        Ins_v = self.__dict__.copy()
        Ins_v["__class__"] = self.__class__.__name__
        Ins_v["created_at"] = self.created_at.isoformat()
        Ins_v["updated_at"] = self.updated_at.isoformat()
        return Ins_v

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


