from fastapi import FastAPI
from core.config import settings

app=FastAPI(title=settings.PROYECT_TITTLE, version=settings.PROYECT_VERSION)

@app.get("/")
def hello():
    return {"msg" : "Hello Fastapi 🚀"}
    