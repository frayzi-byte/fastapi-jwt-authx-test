from sqlalchemy import Column, String, Integer, Text
from app.core.database import Base

class NewUser(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    password_hash = Column(Text, nullable=False) 