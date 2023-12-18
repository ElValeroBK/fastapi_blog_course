from fastapi import FastAPI, HTTPException, status, Depends

development_db = ["DN for Development"]

def get_db_session():
    return development_db


app = FastAPI()

@app.post("/items")
def add_item(item: str, db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return {"message": f"added item {item}"}

