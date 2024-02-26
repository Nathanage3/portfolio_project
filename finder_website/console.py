#!/usr/bin/python3
"""Console"""

import cmd
from datetime import datetime
import model
from model.base_model import BaseModel
from model.subscribers import Subscriber
import shlex
import os

classes = {"BaseModel":BaseModel, "Subscribers":Subscriber}


class MyCommand(cmd.Cmd):
  """MyCommand Console"""
  prompt = '(nathan) '
  
  def do_EOF(self, arg):
    """Exits console"""
    return True
  def do_clear(self, arg):
    """Clear the console screen"""
    os.system('clear' if os.name == 'posix' else 'cls')
  
  def emptyline(self):
    """Overwrting the emptyline method"""
    return False
  
  def do_quit(self, arg):
    """QUit the command to exit the program"""
    return True
  
  def _key_value_parser(self, args):
    """Create a dictionary from a list of strings"""
    new_dict = {}
    
    for arg in args:
      if '=' in arg:
        kvp = arg.split('=', 1)
        key =kvp[0]
        value = kvp[1]
        if value[0] == value[-1] == '"':
          value = shlex.split(value)[0].replace('_', ' ')
        else:
          try:
            value = int(value)
          except:
            try:
              value = float(value)
            except:
              continue
        new_dict[key] = value
    return new_dict
    
  def do_create(self, arg):
    """Create a new instance of class"""
    args = arg.split()
    
    if len(args) == 0:
      print("** class name missing **")
      return False
    
    if args[0] in classes:
      new_dict = self._key_value_parser(args[1:])
      instance = classes[args[0]](**new_dict)
    
    else:
      print("** class doesn't exist **")
      return False
    
    print(instance.id)
    instance.save()
  
  def do_show(self, arg):
    """Prints an instance as a string based on the class and id"""
    args = shlex.split(arg)
    if len(args) == 0:
      print("** class name missing **")
      return False
    if args[0] in classes:
      if len(args) > 1:
        key = args[0] + "." + args[1]
        if key in model.storage.all():
          print(model.storage.all()[key])
        else:
          print("** no instance found **")
      else:
        print("** instance id missing **")
    else:
      print("** class doesn't exist **") 
  
  def do_destroy(self, arg):
    """Deletes an instance based on the class and id"""
    args = shlex.split(arg)
    if len(args) == 0:
      print("** class name missing **")
    elif args[0] in classes:
      if len(args) > 1:
        key = args[0] + "." + args[1]
        if key in model.storage.all():
          model.storage.all().pop(key)
          model.storage.save()
        else:
          print("** no instance found **")
      else:
          print("** instance id missing **")
    else:
      print("** class doesn't exist **")

  def do_all(self, arg):
    """Prints string representations of instances"""
    args = shlex.split(arg)
    obj_list = []
    if len(args) == 0:
      obj_dict = model.storage.all()
    elif args[0] in classes:
      obj_dict = model.storage.all(classes[args[0]])
    else:
      print("** class doesn't exist **")
      return False
    for key in obj_dict:
      obj_list.append(str(obj_dict[key]))
      print("[", end="")
      print(", ".join(obj_list), end="")
      print("]")  
    
  
if __name__ == '__main__':
    MyCommand().cmdloop()

    
        
      