from typing import List
from fastapi import APIRouter

route = APIRouter()

from models.schemas.users import UserCreate, UserRead

from services.user_service import DPUserService

@route.get("/", response_model=List[UserRead])
def get_all(user_service: DPUserService):
    return user_service.get_all()

@route.get("/{id}", response_model=UserRead)
def get_by_id(id: int, user_service: DPUserService):
    return user_service.get(id)

@route.post("/", response_model=UserRead)
def create(user: UserCreate, user_service: DPUserService):
    return user_service.create(user)

@route.put("/{id}", response_model=UserRead)
def update(id: int, user: UserCreate, user_service: DPUserService):
    return user_service.update(id, user)

@route.delete("/{id}")
def delete(id: int, user_service: DPUserService):
    return user_service.delete(id)