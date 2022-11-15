from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .hashing import get_password_hash
from .models import User
from .schemas import UserCreate


def get_all_users(db: Session) -> List[User]:
    """Get all users. """
    return db.query(User).all()


def get_user(db: Session, user_data: dict) -> User:
    """Get user with given data. If there is no any user with given data then raise 404 exception. """
    user = db.query(User).filter_by(**user_data).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cannot find any user with given data')

    return user


def register_new_user(db: Session, request: UserCreate) -> User:
    """Create new user and return refreshed item. """
    new_user = User(
        email=request.email,
        name=request.name,
        password=get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
