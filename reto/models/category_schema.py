from pydantic import BaseModel


class CategoryRead(BaseModel):
    id: int
    name: str
    description: str

class CategoryCreate(BaseModel):
    name: str
    description: str   