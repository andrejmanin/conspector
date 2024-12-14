import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import user_router as UserRouter
from routers import topic_router as TopicRouter
from db.database import SessionLocal, engine, base

base.metadata.create_all(bind=engine)
app = FastAPI()

origins = "*"


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter.router, prefix="/user")
app.include_router(TopicRouter.router, prefix="/topic")

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=1407, reload=True, workers=3)