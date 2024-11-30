from typing import Annotated
from fastapi import Depends, HTTPException, status

from sqlmodel import select

from database.db import DBSession
from models.entities.category import Category
from models.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate

class CategoryService:
    def __init__(self, db: DBSession) -> None:
        self.db = db
        

    def get_all(self):
        categories = self.db.exec(select(Category)).all()
        return categories


    def get_by_id(self, id: int):
        category = self.db.get(Category, id)

        if category == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")

        return category

    def create(self,category_data:CategoryCreate):
        category = Category.model_validate(category_data.model_dump())
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def update(self,id:int ,category_data:CategoryUpdate):
        category_db = self.db.get(Category, id)
        if category_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")
        
        category_db_dict= category_data.model_dump(exclude_unset=True)
        category_db.sqlmodel_update(category_db_dict)
        self.db.add(category_db)
        self.db.commit()
        self.db.refresh(category_db)
        return category_db


    def delete_category(self, id:int):
        category_db = self.db.get(Category, id)

        if category_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")
        self.db.delete(category_db)
        self.db.commit()
        return{"detail":"Category deleted"}

DPCategoryService = Annotated[CategoryService, Depends(CategoryService)]