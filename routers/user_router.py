from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db

from services import services as UserService
from dto import user_class as userDTO

router = APIRouter()

@router.post("/create_user", tags=["user"])
async def create_user(data: userDTO.User = None, db: Session = Depends(get_db)):
    if data is None:
        return None
    return UserService.create_user(data, db)

@router.get("/get_user", tags=["user"])
async def get_user(id: int, db: Session = Depends(get_db)):
    if id is None:
        return None
    return UserService.get_user(id, db)

@router.delete("/delete_user", tags=["user"])
async def delete_user(id: int, db: Session = Depends(get_db)):
    if id is None:
        return None

    user = UserService.get_user(id, db)
    if user is None:
        return None

    UserService.remove_user(id, db)
    return {"message": "deleted"}
