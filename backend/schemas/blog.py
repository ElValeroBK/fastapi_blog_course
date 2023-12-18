from pydantic import BaseModel, root_validator
from datetime import datetime


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str|None = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values:
            values["slug"] = values.get("tittle").replace(" ","-").lower()
        return values

class UpdateBlog(CreateBlog):
    pass

class DealteBlog(CreateBlog):
    pass

class ShowBlog(BaseModel):
    tittle:str
    content: str|None
    created_at: datetime

    class Config():
        orm_mode = True
        
        