#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_type = getenv("STORAGE__TYPE")

if storage_type == "db":
    from model.engine.db_storage import Storage_db
    storage = Storage_db()
else:
    from model.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
