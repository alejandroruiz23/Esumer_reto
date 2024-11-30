from fastapi import APIRouter

from reto.models.schemas.category import CategoryRead,CategoryCreate
from services.category_service import DPCategoryService


route = APIRouter()

@route.get("/categories", response_model=CategoryRead)
async def get_all(category_service: DPCategoryService):
    return category_service.get_all()

@route.get("/categories/{id}", response_model=CategoryRead)
async def get_by_id(id: int, category_service: DPCategoryService):
    category_db = category_service.get_by_id(id)
    return category_db

@route.post("/categories", response_model=CategoryCreate)
def create(category_data,category_service: DPCategoryService):
    category = category_service.create(category_data)
    return category

@route.put("/")
def update():
    pass

@route.delete("/")
def delete():
    pass