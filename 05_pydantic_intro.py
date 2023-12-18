from pydantic import BaseModel, Field
from typing import Optional,List
from enum import Enum
from datetime import datetime


class Comment(BaseModel):
    text : Optional[str] = None
    


class Lenguage(str,Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

class Blog(BaseModel):
    title: str = Field(min_length=7)
    description: Optional[str] = None
    is_active: bool
    lenguage: Lenguage = Lenguage.JAVA
    creat_at: datetime = Field(default_factory=datetime.now)
    comments : Optional[List[Comment]]


first_blog = Blog(title="My title",is_active= True,comments=[{"text" : "Mi first comment"}])
print(first_blog)

import time
time.sleep(2)

second_blog = Blog(title="My title",is_active= True,comments=[{"text" : "Mi second comment"}])
print(second_blog)