from fastapi import APIRouter

route = APIRouter()

@route.post("/sign-up")
def sign_up():
    pass

@route.post("/login")
def login():
    pass

@route.post("/logout")
def logout():
    pass