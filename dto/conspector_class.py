from pydantic import BaseModel


class Conspector(BaseModel):
    grade: int
    science: str
    topic: str
    text: str