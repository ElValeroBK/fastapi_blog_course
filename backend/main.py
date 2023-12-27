from fastapi import FastAPI
from core.config import settings
from db.session import engine 
from db.base import Base
from apis.base import api_router
from apps.base import app_router
from fastapi.staticfiles import StaticFiles

def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)

def configure_staticfile(app:FastAPI):
    app.mount("/static",StaticFiles(directory="static"),name="static")
    


# alembic is creating de tables now
    
# def create_tables():         
# 	Base.metadata.create_all(bind=engine)
      

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    configure_staticfile(app)

    #create_tables()
    
    return app


app = start_application()


# app = FastAPI()


# @app.get("/")
# def hello():
#     return {"msg" : "Hello Fastapi 🚀"}
    