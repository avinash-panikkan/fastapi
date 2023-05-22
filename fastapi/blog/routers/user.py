from fastapi import APIRouter, Depends, status
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['Users'],
)


@router.post('/', response_model= schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)
    

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)