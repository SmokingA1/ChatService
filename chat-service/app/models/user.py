from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True, index=True)
    hashed_pass = Column(String, nullable=False)

    messages = relationship("Message", back_populates='sender')