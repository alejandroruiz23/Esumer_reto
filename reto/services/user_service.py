from typing import Annotated
from fastapi import Depends, HTTPException, status

from sqlmodel import select

from models.entities.users import Users
from models.schemas.users import UserRead, UserCreate

from database.db import DBSession

class UserService:
    def __init__(self, db: DBSession):
        self.db = db

    def get_all(self):
        return self.db.exec(select(Users)).all() or []

    def get(self, id: int):
        user = self.db.get(Users, id)

        if user == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
        
        user_read = UserRead(
            id=id,
            username=user.username,
            password=user.password,
            full_name=user.full_name,
            role=user.role,
            permissions=user.permissions,
        )

        return user_read

    def create(self, user: UserCreate):
        user_db = Users.model_validate(user.model_dump())
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)

        user_read = UserRead(
            id=user_db.id,
            role=user_db.role,
            permissions=user_db.permissions, 
            username=user_db.username,
            full_name=user_db.full_name,
            password=user_db.password
        )
        return user_read

    def update(self, id: int, user: UserCreate):
        user_db = self.db.get(Users, id)

        if user_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

        user_db.username = user.username
        user_db.password = user.password
        user_db.full_name = user.full_name
        self.db.add(user_db)
        self.db.commit()
        
        user_read = UserRead(
            id=user_db.id,
            role=user_db.role,
            permissions=user_db.permissions, 
            username=user_db.username,
            full_name=user_db.full_name,
            password=user_db.password
        )
        return user_read

    def delete(self, id: int):
        user = self.db.get(Users, id)

        if user == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
        
        self.db.delete(user)
        self.db.commit()
        return {"message": "Product deleted", "status": "success"}

DPUserService = Annotated[UserService, Depends(UserService)]
