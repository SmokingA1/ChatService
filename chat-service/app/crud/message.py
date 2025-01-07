from sqlalchemy.orm import Session
from models.message import Message
from schemas.message import MessageCreate, MessageRead, MessageUpdate
from typing import List, Optional

#get message 
def get_message_by_id(message_id: int, db: Session) -> Optional[MessageRead]:
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if db_message:
        return MessageRead.from_orm(db_message)
    return None

#get messages
def get_messages(db: Session) -> List[MessageRead]:
    return db.query(Message).all()

#Create message
def create_message(message_create: MessageCreate, db: Session) -> Optional[MessageRead]:
    new_message = Message(**message_create.dict())

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message

#Update message
def update_message(message_id: int, message_update: MessageUpdate, db:Session) -> Optional[MessageRead]:
    db_message = get_message_by_id(message_id, db)
    if not db_message:
        return None
    if message_update.content:
        db_message.content = message_update.content
    db.commit()
    db.refresh(db_message)
    return db_message
    
#Delete message
def delete_message(message_id: int, db: Session) -> Optional[MessageRead]:
    db_message = get_message_by_id(message_id, db)
    if not db_message:
        return None
    
    db.delete(db_message)
    db.commit()
    return db_message