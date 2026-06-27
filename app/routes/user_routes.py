from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user_schemas import (
    UserCreate,
    UserResponse
)

from app.repositories.user_repositories import(
    get_users,
    create_user,
    delete_user,
    login
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def get_all_users(db : Session = Depends(get_db)):
    return get_users(db)

@router.get("/login", response_model=UserResponse)
def login_user(user : UserCreate, db : Session = Depends(get_db)):
    return login(db, user)

@router.post("/", response_model=UserResponse)
def register(user : UserCreate, db : Session = Depends(get_db)):
    return create_user(db, user)

@router.delete("/{user_id}")
def delete_one_user(user_id : int, db : Session = Depends(get_db)):
    return delete_user(db, user_id)