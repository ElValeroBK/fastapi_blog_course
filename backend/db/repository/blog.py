from typing import List
from sqlalchemy.orm import Session
from schemas.blog import CreateBlog,UpdateBlog, DealteBlog
from db.models.blog import Blog




def create_new_blog(blog:CreateBlog, db:Session, autor_id:int = 1):
    blog = Blog(
        title =blog.title,
        slug = blog.slug,
        content = blog.content,
        autor_id=autor_id,
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return db

def retreive_blog(id :int ,db:Session):
    blog = db.query(Blog).filter(Blog.id==id).first()
    return blog


def reteive_all_blog(db:Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs
 

def update_a_blog_by_id(id: int,blog:UpdateBlog, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id==id).first()
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db

def delate_a_blog_by_id(id:int, db:Session, author_id: int):
    blog_in_db= db.query(Blog).filter(Blog.id==id)
    if not blog_in_db.first():
        return {"error", f"Could not find blod with the id {id}"}
    blog_in_db.delete()
    db.commit()
    return {"msg",f"Delated blog with id {id}"}

