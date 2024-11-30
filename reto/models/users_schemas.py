from sqlmodel import SQLModel

class UsersCreate(SQLModel):
    username:str
    password:str
    full_name:str

class UsersCreate(SQLModel):
    id:int
    username:str
    password:str
    full_name:str
    role:str
    permissions:str


class AuthLogin(SQLModel):
    username:str
    password:str


class AuthRegister(SQLModel):
    pass