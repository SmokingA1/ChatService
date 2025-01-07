from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    pass

class MessageRead(MessageBase):
    id: int
    timestamp: datetime
    sender_id: int 

    class Config:
        orm_mode = True

class MessageUpdate(BaseModel):
    content: Optional[str] = None

