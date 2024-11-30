from sqlmodel import SQLModel

class UserCreate(SQLModel):
    username:str
    password:str
    full_name:str

class UserRead(SQLModel):
    id: int
    username: str
    password: str
    full_name: str
    role: str
    permissions: str

class AuthLogin(SQLModel):
    username:str
    password:str

class AuthRegister(SQLModel):
    pass