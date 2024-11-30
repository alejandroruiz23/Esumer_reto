from sqlmodel import SQLModel

'''

'''
class CategoryRead(SQLModel):
    id: int
    name: str
    description: str

class CategoryCreate(SQLModel):
    name: str
    description: str   