#!/usr/bin/python3
"""FileStorage class"""

import json
import model
from model.base_model import BaseModel
from model.subscribers import Subscriber

classes = {"BaseModel":BaseModel, "Subscriber":Subscriber}


class FileStorage:
  
  """Serializes instances to a JSON file and
     deserializes back to instances
  """
  __file_path = "file.json"
  __objects = {}
  def all(self, cls=None):
    """Return the dictionary __objects"""
    if cls is not None:
      new_dict = {}
      for key, value in self.__objects.items():
        if cls == value.__class__ or cls == value.__class__.__name__:
         new_dict[key] = value
      return new_dict
    return self.__objects
  
  def new(self, obj):
    """Sets in __objects, the obj with key <obj class name>.id"""
    if obj is not None:
      key = obj.__class__.__name__ + "." + obj.id
      self.__objects[key] = obj
      
  '''def save(self):
    """serializes __objects to the JSON file (path: __file_path)"""
    json_objects = {}
    for key in self.__objects:
      if "password" in self.__objects[key].to_dict(save_fs=1):
        self.__objects[key].to_dict(save_fs=1)["password"] = self.__objects[key].to_dict(save_fs=1)["password"].decode()
        
        #json_objects[key].decode()
      json_objects[key] = self.__objects[key].to_dict(save_fs=1)
    with open(self.__file_path, 'w') as f:
      json.dump(json_objects, f)
     '''
     
  def save(self):
    """serializes __objects to the JSON file (path: __file_path)"""
    json_objects = {}
    for key in self.__objects:
      if key == "password":
        json_objects[key].decode()
      #json_objects[key] = self.__objects[key].to_dict(save_fs=1)
      json_objects[key] = self.__objects[key].to_dict(save_fs=1)

    with open(self.__file_path, 'w') as f:
      json.dump(json_objects, f)
         
  def reload(self):
    """Deserializes the JSON file to __objects"""
    try:
      with open(self.__file_path, 'r') as f:
        jsn = json.load(f)
        for key, value in jsn.items():
          class_name = value["__class__"]
          obj = classes[class_name](**value)
          self.__objects[key] = obj
        
    except Exception as e:
      print(f"Error reloading: {e}")
        
  def delete(self, obj=None):
    """Delete obj from __objects if it exists"""
    if obj is not None:
      key = obj.__class__.__name__ + '.' + obj.id
      if key in self.__objects:
        del self.__objects[key]
    
  def close(self):
    """Call relaod() method for deserializing"""
    self.reload()
    
  def get(self, cls, id):
    """Return the object based on the class name
       and its ID, or None if not found    
    """
    if cls not in classes.values():
      return None
    
    all_cls = model.storage.all(cls)
    for value in all_cls.values():
      if (value.id == id):
        return value
      
  def count(self, cls=None):
    """Count the number of objects"""
    all_class = classes.values
    if not cls:
      count = 0
      for clas in all_class:
        count += len(model.storage.all(cls))
        
    else:
      count = len(model.storage.all(cls).values())
      return count
      
      