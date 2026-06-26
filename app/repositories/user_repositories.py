from sqlalchemy.orm import Session
from app.models.user_model import NewUser
from app.schemas.user_schemas import UserCreate
from app.utils.security import hash_password

def get_users(db : Session):
    return db.query(NewUser).all()

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
    db.refresh(user)
    return user