from sqlmodel import select
from database.db import DBSession
from reto.models.category_model import Category


class CategoryService():
    def __init__(self, db: DBSession):
        self.db = db

    def get_all_categories(self):
        categories = self.db.exec(select(Category).all())
        return categories
