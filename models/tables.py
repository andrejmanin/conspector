from sqlalchemy import Column, Integer, String
from db.database import base

class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


class ConspectorModel(base):
    __tablename__ = 'conspector_text'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    grade = Column(Integer, nullable=False)
    science = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    text = Column(String)

