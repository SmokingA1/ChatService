from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User
from schemas.user import UserCreate, UserUpdate, UserRead
from typing import List
#get user 
async def get_user_by_id(user_id: int, db: AsyncSession) -> UserRead:
    user = await db.execute(select(User).filter(User.id == user_id)) 
    db_user = user.scalars().first()
    return UserRead.from_orm(db_user)

#get all users
async def get_users(db: AsyncSession) -> List[UserRead]:
    users = await db.execute(select(User))
    db_users = users.scalars().all()
    return [UserRead.from_orm(user) for user in db_users]

#create user
async def create_user(user: UserCreate, db: AsyncSession) -> UserRead:
    new_user = User(**user.dict())
    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
    except:
        db.rollback()
        raise ValueError("Error creating user, check data.")
    
    return new_user

#update user
async def update_user(user_update: UserUpdate, user_id: int, db: AsyncSession) -> UserRead:
    db_user = await get_user_by_id(user_id, db)
    if not db_user:
        return None
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    
    await db.commit()
    await db.refresh(db_user)
    return db_user

#delete user
async def delete_user(user_id: int, db:AsyncSession) -> UserRead:
    db_user = await get_user_by_id(user_id, db)
    if not db_user:
        return None
    await db.delete(db_user)
    await db.commit()
    return db_user