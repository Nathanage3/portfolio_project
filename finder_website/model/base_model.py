#!/usr/bin/python3
"""A Base model class for all other classes"""
''''
from datetime import datetime
import model
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M-%S.%f"

if model.storage_type == "db":
  Base = declarative_base()
else:
  Base = object
  
class BaseModel(Base):
  """A BaseModel class for all other classes"""
  if model.storage_type == "db":
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
  def __init__(self, *args, **kwargs):
    """Initialization of the Basemodel class"""
    if kwargs:
        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)
        if kwargs.get("created_at", None) and type(self.created_at) is str:
            self.created_at = datetime.strptime(kwargs["created_at"], time)
        else:
            self.created_at = datetime.utcnow()  # Note the function call here
        if kwargs.get("updated_at", None) and type(self.updated_at) is str:
            self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.updated_at = datetime.utcnow()  # Note the function call here
        if kwargs.get("id", None) is None:
            self.id = str(uuid.uuid4())
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

  
  def __str__(self):
    """String Representation of Basemodel"""
    return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
  
  def to_dict(self, save_fs=None):
    """Returns a dictionary containing all keys/values of the instance"""
    new_dict = self.__dict__.copy()
    if "created_at" in new_dict and isinstance(new_dict["created_at"], datetime):
        new_dict["created_at"] = new_dict["created_at"].strftime(time)

    if "updated_at" in new_dict and isinstance(new_dict["updated_at"], datetime):
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
    new_dict["__class__"] = self.__class__.__name__
    if "_sa_instance_state" in new_dict:
        del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
            return new_dict

  def save(self):
    """Updates the attribute 'updated_at' with the current datetime"""
    self.updated_at = datetime.utcnow()
    model.storage.new(self)
    model.storage.save()

  def delete(self):
    """delete the current instance from the storage"""
    model.storage.delete(self) '''
    

from datetime import datetime
import model
import uuid
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

time = "%Y-%m-%dT%H:%M-%S.%f"

if model.storage_type == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel():
    """A BaseModel class for all other classes"""
    if model.storage_type == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the Basemodel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String Representation of Basemodel"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                        self.__dict__)

    def to_dict(self, save_fs=None):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict and isinstance(new_dict["created_at"], datetime):
            new_dict["created_at"] = new_dict["created_at"].strftime(time)

        if "updated_at" in new_dict and isinstance(new_dict["updated_at"], datetime):
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
            if save_fs is None:
                if "password" in new_dict:
                    del new_dict["password"]
                return new_dict

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        model.storage.new(self)
        model.storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        model.storage.delete(self)