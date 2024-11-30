from enum import Enum
from sqlmodel import SQLModel
from pydantic import Field


class RoleEnum(str, Enum):
    ADMIN = "admin"
    GENERAL = "general"

class PermissionsEnum(str, Enum):
    VIEW = "ver"
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
    role: RoleEnum = Field(default=RoleEnum.GENERAL)
    permissions: PermissionsEnum = Field(default=PermissionsEnum.EDIT)

