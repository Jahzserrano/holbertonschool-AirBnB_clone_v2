#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    def __init__(self, name, state_id,
                 created_at, updated_at, *args, **kwargs):
        super().__init__(id, created_at, updated_at, *args, **kwargs)
        self.name = name
        self.state_id = state_id
