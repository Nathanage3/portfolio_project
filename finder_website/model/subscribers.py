#!/usr/bin/python3
"""Holds class Subscriber"""

import model
from model.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

class Subscriber(BaseModel, Base):
  """Representation of state"""
  if model.storage_type == "db":
    __tablename__ = 'subscribers'
    username = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    
  else:
    username = ""
    password = ""
  '''  
  def __init__(self, *args, **kwargs):
    """Initialization of subscribers class"""
    super().__init__(*args, **kwargs)
  '''

def __init__(self, *args, **kwargs):
    """Initialization of subscribers class"""
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
        
        # Handle password format if it exists
        if "password" in kwargs:
            self.password = kwargs["password"]
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
