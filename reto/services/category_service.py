from typing import Annotated
from fastapi import Depends, HTTPException, status

from sqlmodel import select

from database.db import DBSession
from reto.models.entities.category import Category
from reto.models.schemas.category import CategoryRead

class CategoryService:
    def __init__(self, db: DBSession) -> None:
        self.db = db
        self.Categoryategory = Category

    def get_all(self):
        categories = self.db.exec(select(Category).all())
        return categories


    def get_by_id(self, id: int):
        category = self.db.get(Category, id)

        if category == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")

        return category

    def create(self,category_data):
        category = Category.model_validate(category_data.model_dump())
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def update():
        pass

    def delete():
        pass

DPCategoryService = Annotated[CategoryService, Depends(CategoryService)]