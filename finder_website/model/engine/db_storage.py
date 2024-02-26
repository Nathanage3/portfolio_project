#!/usr/bin/python3
"""Database Storage class Storage_db"""

import model
from model.base_model import BaseModel, Base
from model.subscribers import Subscriber
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {"BaseModel":BaseModel, "Subscriber":Subscriber}


class Storage_db:
  """Intercts with the MySQL"""
  __engine = None
  __session = None
  
  def __init__(self):
    """Instantiate a Storage_db object"""
    MYSQL_USER = getenv('MYSQL_USER')
    MYSQL_PWD = getenv('MYSQL_PWD')
    MYSQL_HOST = getenv('MYSQL_HOST')
    MYSQL_DB = getenv('MYSQL_DB')
    ENV = getenv('ENV')
    
    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                  format(MYSQL_USER,
                                         MYSQL_PWD,
                                         MYSQL_HOST,
                                         MYSQL_DB,
                                         pool_pre_ping=True))
  def all(self, cls=None):
    """Query on the current database session"""
    new_dict = {}
    for cl in classes:
      if cl is None or cl is classes[cl] or cls is cl:
        objs = self.__session.query(classes[cl]).all()
        for obj in objs:
          key = obj.__class__.__name__ + '.' + obj.id
          new_dict[key] = obj
    return (new_dict)
      
  def new(self, obj):
    """Add the object to the current database session"""
    self.__session.add(obj)
    
  def save(self):
    """Commit all changes of the current database session"""
    self.__session.commit()
    
  def reload(self):
    """Relaods data from the database"""
    Base.metadata.create_all(self.__engine)
    sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
    Session = scoped_session(sess_factory)
    self.__session = Session
    
    
  def close(self):
    """Call remove() method on the private session attribute"""
    self.__session.remove()
    
  def get(self, cls, id):
    """Returns the object based on the class name 
       and its ID, or None if not found 
    """ 
    if cls not in classes.values():
      return None
    all_cls = model.storage.all(cls)
    for value in all_cls.values():
      if (value.id == id):
        return value
      
    return None
  
  def count(self, cls=None):
    """Count the number of objects in storage"""
    all_class = classes.values()
    
    if not cls:
      count = 0
      for clss in all_class:
        count += len(model.storage.all(clss).values())
    else:
      count = len(model.storage.all(clss).values())
    return count  
      
    
  