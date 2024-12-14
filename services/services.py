from dto import user_class, conspector_class
from dto.conspector_class import Conspector
from models.tables import User, ConspectorModel
from sqlalchemy.orm import Session
import traceback

def create_user(data: user_class.User, db: Session):
    user = User(name=data.name, email=data.email, password=data.password)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as ex:
        print(ex)
    return user

def get_user(id: int, db):
    return db.query(User).filter(User.id == id).first()

def remove_user(id: int, db):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return user

def create_topic(data: conspector_class.Conspector, db: Session):
    topic = ConspectorModel(grade=data.grade, science=data.science, topic=data.topic, text=data.text)
    try:
        db.add(topic)
        db.commit()
        db.refresh(topic)
    except Exception as ex:
        traceback.print_exception(ex)
        return {"message": "Topic creation failed"}
    return topic

def get_topic(science: str, grade: int, topic: str, db: Session):
    return db.query(ConspectorModel).filter(
        (ConspectorModel.science == science) &
        (ConspectorModel.grade == grade) &
        (ConspectorModel.topic == topic)
    ).first()


def add_text(data: conspector_class.Conspector, db: Session):
    topic = db.query(ConspectorModel).filter(
        (ConspectorModel.topic == data.topic) &
        (ConspectorModel.grade == data.grade) &
        (ConspectorModel.topic == data.topic)
    ).first()

    if topic is None:
        return {"message": "No topic found"}
    topic.text = data.text
    try:
        db.add(topic)
        db.commit()
        db.refresh(topic)
    except Exception as ex:
        print(ex)
    return topic
