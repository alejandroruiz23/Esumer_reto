from fastapi import APIRouter

route = APIRouter()

@route.get("/")
def get():
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