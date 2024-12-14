from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from services import services as UserService
from dto import conspector_class as conspectorDTO

router = APIRouter()

@router.post("/create_topic", tags=["topic"])
async def create_topic(data: conspectorDTO.Conspector = None, db: Session = Depends(get_db)):
    if(data is None):
        return None
    return UserService.create_topic(data, db)

@router.get("/get_topic", tags=["topic"])
async def get_topic(science: str, grade: int, topic: str, db: Session = Depends(get_db)):
    if grade is None or science is None or topic is None:
        return None
    return UserService.get_topic(science, grade, topic, db)

@router.post("/add_text", tags=["topic"])
async def add_text(data: conspectorDTO.Conspector, db: Session = Depends(get_db)):
    if data is None:
        return None
    return UserService.add_text(data, db)
