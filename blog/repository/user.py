


from sqlalchemy.orm import Session
from .. import Models, schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def createUser(request: schemas.User,db:Session):
    new_user = Models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def showUser(id:int,db:Session):
    user = db.query(Models.User).filter(Models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user