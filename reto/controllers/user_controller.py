from fastapi import APIRouter

route = APIRouter()

from models.schemas.users import UsersCreate 

from services.user_service import DPUserService

@route.get("/")
def get_all(user_service: DPUserService):
    return user_service.get_all()

@route.get("/{id}")
def get_all(id: int, user_service: DPUserService):
    return user_service.get(id)

@route.post("/")
def create(user: UsersCreate, user_service: DPUserService):
    return user_service.create(user)

@route.put("/{id}")
def update(id: int, user: UsersCreate, user_service: DPUserService):
    return user_service.update(id, user)

@route.delete("/{id}")
def delete(id: int, user_service: DPUserService):
    return user_service.delete(id)