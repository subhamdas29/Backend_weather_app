from fastapi import APIRouter,Depends,HTTPException,status
import schemas
from db import get_db
from sqlalchemy.orm import Session
import models
from hashing import Hash
from JWToken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.post("/login")
def login(request: OAuth2PasswordRequestForm=Depends() , db: Session = Depends(get_db)):
    user =db.query(models.User).filter(models.User.username==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
