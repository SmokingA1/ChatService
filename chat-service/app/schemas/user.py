from pydantic import BaseModel
from typing import Optional
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    hashed_pass: str

class UserRead(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    hashed_pass: Optional[str] = None