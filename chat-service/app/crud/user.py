from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate, UserRead
from typing import List
#get user 
def get_user_by_id(user_id: int, db: Session) -> UserRead:
    return db.query(User).filter(User.id == user_id).first()

#get all users
def get_users(db: Session):
    return db.query(User).all()

#create user
def create_user(user: UserCreate, db: Session) -> List[UserRead]:
    new_user = User(**user.dict())
    try:
        db.commit()
        db.refresh(new_user)
    except:
        db.rollback()
        raise ValueError("Error creating user, check data.")
    
    return new_user

#update user
def update_user(user_update: UserUpdate, user_id: int, db: Session) -> UserRead:
    db_user = get_user_by_id(user_id, db)
    if not db_user:
        return None

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

#delete user
def delete_user(user_id: int, db:Session) -> UserRead:
    db_user = get_user_by_id(user_id, db)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user