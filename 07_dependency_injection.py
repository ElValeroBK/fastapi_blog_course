
from fastapi import FastAPI, Depends, status, HTTPException
from typing import Annotated

app = FastAPI(title= "Dependency and injection")

blogs = {
    "1":"fastapi",
    "2":"pydantic",
    "3":"basemodel"
}
users = {
    "8": "Yasiel",
    "9": "danay"
}

class GetObjetOr404:
    def __init__(self,model:str,name:str) -> None:
        self.model = model
        self.name = name

    def __call__(self, id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(detail=f"{self.name} with id {id} does not exist",
                            status_code=status.HTTP_404_NOT_FOUND)
        return obj

get_blog= GetObjetOr404(blogs,"blog")
get_user= GetObjetOr404(users,"user")

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str , Depends(get_blog)]):
    return blog_name

@app.get("/user/{id}")
def get_blog(user_name: Annotated[str , Depends(get_user)]):
    return (user_name)