from fastapi import APIRouter , Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from db.session import get_db
from core.security import create_access_token
from core.hashing import Hasher
from core.config import settings
from db.repository.login import get_user_by_email



router = APIRouter()


def authenticate_user(email:str, password:str, db:Session):
    user = get_user_by_email(email=email,db=db)
    if not user:
        return False
    if not Hasher.verify_password(password,user.password):
        return False
    return user



@router.post("/token")
def login_for_access_token(form_data:OAuth2PasswordRequestForm= Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(detail="Incoreect email or password",status_code=status.HTTP_401_UNAUTHORIZED)
    
    access_token = create_access_token(data={"sub":user.email})
    return {"access_token": access_token,"token_type":"bearer"}   

oauth2_escheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_user(token:str= Depends(oauth2_escheme), db:Session = Depends(get_db)):
    Credentials_exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="could not validate the credentials please login again"
                                         )
    
    try:
       pay_load = jwt.decode(token,settings.SECRET_KEY,settings.ALGRITHM)
       email: str = pay_load.get({"sub"})
       if not email:
           raise Credentials_exeption
    except JWTError:
        raise Credentials_exeption
    user = get_user_by_email(email=email,db=db)
    if user is None:
        raise Credentials_exeption
    return user
    



    

