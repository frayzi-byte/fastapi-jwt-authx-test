from sqlalchemy.orm import Session
from app.models.user_model import NewUser
from app.schemas.user_schemas import UserCreate
from app.utils.security import hash_password, verify_password

def get_users(db : Session):
    return db.query(NewUser).all()

def login(db : Session, user : UserCreate):

    found_user = db.query(NewUser).filter(NewUser.name == user.name).first()

    if not found_user:
        return {"User not found!"}

    if not verify_password(user.password, found_user.password_hash):
        return {"Password is incorrect"}
    
    return found_user

def create_user(db : Session, user : UserCreate):
    password_hash = hash_password(
        user.password
    )

    db_user = NewUser(
        name = user.name,
        password_hash=password_hash,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db : Session, user_id : int):
    user = db.query(NewUser).filter(NewUser.id == user_id).first()
    if not user:
        return None
    
    db.delete(user)
    db.commit()
    db.refresh(user)
    return user