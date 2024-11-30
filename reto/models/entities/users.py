from enum import Enum
from sqlmodel import SQLModel, Field

class RoleEnum(str, Enum):
    ADMIN = "admin"
    GENERAL = "general"

class PermissionsEnum(str, Enum):
    READ = "leer"
    EDIT = "editar" 

'''Esta clase permite crear la tabla curso en la base de datos
    id de la categoria
    nombre de la categoria
    descripcion de la categoria
'''
class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    full_name: str
    role: str = Field(default="admin")
    permissions: str = Field(default="editar")

