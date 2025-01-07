from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.message import Message
from schemas.message import MessageCreate, MessageRead, MessageUpdate
from typing import List, Optional

#get message 
async def get_message_by_id(message_id: int, db: AsyncSession) -> Optional[MessageRead]:
    message = await db.execute(select(Message).filter(Message.id == message_id))
    db_message = message.scalars().first()
    if db_message:
        return MessageRead.from_orm(db_message)
    return None

#get messages
async def get_messages(db: AsyncSession) -> List[MessageRead]:
    messages = await db.execute(select(Message))
    db_messages = messages.scalars.all()
    return [MessageRead.from_orm(message) for message in db_messages]

#Create message
async def create_message(message_create: MessageCreate, db: AsyncSession) -> Optional[MessageRead]:
    new_message = Message(**message_create.dict())

    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)

    return new_message

#Update message
async def update_message(
        message_id: int, message_update: MessageUpdate,
        db:AsyncSession) -> Optional[MessageRead]:
    db_message = await get_message_by_id(message_id, db)
    if not db_message:
        return None
    if message_update.content:
        db_message.content = message_update.content
    await db.commit()  
    await db.refresh(db_message)  
    return db_message
    
#Delete message
async def delete_message(message_id: int, db: AsyncSession) -> Optional[MessageRead]:
    db_message = await get_message_by_id(message_id, db)
    if not db_message:
        return None
    
    await db.delete(db_message)
    await db.commit()
    return db_message