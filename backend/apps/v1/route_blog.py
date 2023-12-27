from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.blog import reteive_all_blog, retreive_blog

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request, alert: str|None = None, db: Session = Depends(get_db)):
    blogs = reteive_all_blog(db=db)
    context = {"request": request, "blogs": blogs, "alert": alert}

        #print(dir(request))
    return templates.TemplateResponse("blogs/home.html",context=context)


@router.get("/app/blog/{id}")
def blog_detail(id: int, request:Request, db: Session= Depends(get_db)):
    blog = retreive_blog(id=id,db=db)
    context = {"request": request, "blog":blog}

    return templates.TemplateResponse("blog/detail.html",context=context)
