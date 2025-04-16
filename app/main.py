from fastapi import FastAPI, HTTPException
from typing import List
from app.models import User, UserCreate
from app import crud

app = FastAPI()

@app.post("/users", response_model=User)
def create(user: UserCreate):
    return crud.create_user(user)

@app.get("/users", response_model=List[User])
def list_all():
    return crud.list_users()

@app.get("/users/{user_id}", response_model=User)
def get(user_id: int):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
def update(user_id: int, user_data: UserCreate):
    user = crud.update_user(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
def delete(user_id: int):
    if not crud.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
