#!/usr/bin/python3
"""
initialize the models package
"""
HBNB_MYSQL_USER='hbnb_dev' 
HBNB_MYSQL_PWD='hbnb_dev_pwd'
HBNB_MYSQL_HOST='localhost'
HBNB_MYSQL_DB='hbnb_dev_db' 
HBNB_TYPE_STORAGE='db'

from os import getenv
from models.engine.db_storage import DBStorage


# if getenv("HBNB_TYPE_STORAGE") == "db":
#     from models.engine.db_storage import DBStorage
#     storage = DBStorage()

# else:
#     from models.engine.file_storage import FileStorage
#     storage = FileStorage()

storage = DBStorage()
storage.reload()
