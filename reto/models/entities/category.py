from sqlmodel import SQLModel, Field


'''Esta clase permite crear la tabla curso en la base de datos
    id de la categoria
    nombre de la categoria
    descripcion de la categoria
'''

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str



