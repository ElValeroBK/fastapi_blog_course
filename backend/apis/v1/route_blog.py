from typing import List
from fastapi import APIRouter , Depends, status,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog, UpdateBlog, DealteBlog
from db.repository.blog import create_new_blog, retreive_blog, reteive_all_blog, update_a_blog_by_id, delate_a_blog_by_id

router = APIRouter()

@router.post("/",response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog:CreateBlog,db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog,db=db, author_id=1)
    return blog


@router.get("/{id}",response_model=ShowBlog)
def get_Blog(blog:CreateBlog, db:Session = Depends(get_db)):
    blog = retreive_blog(id= int,db= db)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return blog

@router.get("", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = reteive_all_blog(db=db)
    if not blogs:
        raise HTTPException(detail=f"does not exist any blog activet!!!")
    return blogs
   
@router.put("/{id}",response_model=ShowBlog,status_code=status.HTTP_201_CREATED)
def update_blog(id:int, blog:UpdateBlog, db:Session = Depends(get_db)):
    blog = update_a_blog_by_id(id=id, blog=blog, db=db, author_id=1)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)    
    return blog

@router.delete("/{id}")
def delate_blog(id:int, db:Session=Depends(get_db)):
    message= delate_a_blog_by_id(id=id, db=db, author_id=1)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"),status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg",message.get("msg")}
