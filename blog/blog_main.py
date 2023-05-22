from fastapi import FastAPI, Depends 
from typing import List
from . import Models
from .database import engine, get_db


from .routers import blog, user, authentication


app = FastAPI()

Models.Base.metadata.create_all(engine)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


