from fastapi import APIRouter

from models.schemas.category import CategoryRead,CategoryCreate
from services.category_service import DPCategoryService


route = APIRouter()

@route.get("/", response_model=CategoryRead)
async def get_all(category_service: DPCategoryService):
    return category_service.get_all()

@route.get("/{id}", response_model=CategoryRead)
async def get_by_id(id: int, category_service: DPCategoryService):
    category_db = category_service.get_by_id(id)
    return category_db

@route.post("/", response_model=CategoryCreate)
def create(category_data:CategoryCreate,category_service: DPCategoryService):
    category = category_service.create(category_data)
    return category

@route.put("/")
def update():
    pass

@route.delete("/")
def delete():
    pass