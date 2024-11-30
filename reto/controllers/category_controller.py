from fastapi import APIRouter

from reto.models.category_schema import CategoryRead

route = APIRouter()

@route.get("/categories", response_model=CategoryRead)
async def get_category():
    pass

@route.post("/")
def create():
    pass

@route.put("/")
def update():
    pass

@route.delete("/")
def delete():
    pass