from fastapi import APIRouter

from reto.models.category_schema import CategoryRead
from services.category_service import CategoryService


route = APIRouter()

@route.get("/categories", response_model=CategoryRead)
async def get_categories():
    return CategoryService.get_all_categories()

@route.post("/")
def create():
    pass

@route.put("/")
def update():
    pass

@route.delete("/")
def delete():
    pass