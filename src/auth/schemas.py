from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from core.database import get_db
from .models import User


db = next(get_db())


class UserBase(BaseModel):
    name: str


class Login(UserBase):
    password: str = Field(..., min_length=8)

    @validator('name')
    def validate_name(cls, value):
        if not db.query(User).filter(User.name == value).count():
            raise ValueError('Cannot find any user with given name')

        return value


class UserCreate(Login):
    email: str

    @validator('email')
    def validate_email(cls, value):
        if db.query(User).filter(User.email == value).count():
            raise ValueError('This name is already taken')

        return value

    @validator('name')
    def validate_name(cls, value):
        if db.query(User).filter(User.name == value).count():
            raise ValueError('This name is already taken')

        return value


class UserSingle(UserBase):
    id: int
    email: str
    type: str
    is_active: bool = False
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True


class UserList(BaseModel):
    __root__: List[UserSingle]


class Token(BaseModel):
    """Schema with auth token (jwt) data. """
    access_token: str
    token_type: str = 'bearer'


class TokenData(BaseModel):
    """Schema for get_current_user dependency. """
    id: int
    name: Optional[str] = None
