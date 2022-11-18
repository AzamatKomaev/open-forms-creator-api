from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth.jwt import get_current_user
from core.database import get_db
from . import (
    schemas,
    services,
    jwt,
    hashing
)


router = APIRouter()


@router.get('/me', response_model=schemas.UserSingle)
def get_me(db: Session = Depends(get_db),
           current_user: schemas.TokenData = Depends(get_current_user)):
    return services.get_user(db, {'id': current_user.id})


@router.post('/create', response_model=schemas.UserSingle, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = services.register_new_user(db, request)
    return new_user


@router.post('/login', status_code=status.HTTP_201_CREATED)
def login(request: schemas.Login, db: Session = Depends(get_db)):
    """Log in user getting access token (jwt). """
    user = services.get_user(db, {'name': request.name})

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid password')

    access_token = jwt.create_access_token(data={'id': user.id, 'sub': user.name})
    return {'access_token': access_token, 'token_type': 'bearer'}

