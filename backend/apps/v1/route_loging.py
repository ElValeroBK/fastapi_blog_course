import json
from fastapi import APIRouter, responses, Form, Request,status, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.session import get_db
from db.repository.user import create_new_user
from pydantic import ValidationError
from core.security import create_access_token
from apis.v1.route_login import authenticate_user

from core.hashing import Hasher
 


templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/register")
def register(request :Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})


@router.post("/register")
def register(request: Request, email:str = Form(...), password:str = Form(...),db: Session= Depends(get_db)):
    errors =[]
    try:
       # password_hash =  Hasher.get_password_hash(password=password)
        user = UserCreate(email=email,password=password)
        create_new_user(user=user, db=db)
        return responses.RedirectResponse("/?alert=Successfully%Registered",status_code=status.HTTP_302_FOUND)
    except ValidationError as e:
        errors_list = json.loads(e.json())
        for item in errors_list:
            errors.append(item.get("loc")[0]+": "+item.get("msg"))
        return templates.TemplateResponse("auth/register.html",{"request": request, "errors": errors})
        


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html",{"request": request})

@router.post("/login")
def login(request:Request, email:str = Form(...), password: str= Form(...), db: Session= Depends(get_db)):

    errors = []
    user = authenticate_user(email=email, password=password,db=db)
    if  not user:
        errors.append("Incorrect email or password")
        return templates.TemplateResponse("auth/login.html", {"request": request, "errors": errors, "email": email})
    
    access_token = create_access_token(data={"sub":email})
    response = responses.RedirectResponse("/?alert=successfully Logged In",status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}")
    return response





    


