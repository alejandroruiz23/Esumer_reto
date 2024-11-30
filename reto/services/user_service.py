from typing import Annotated
from fastapi import Depends

from sqlmodel import select

from database.db import DBSession

class UserService:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    def get_all():
        pass

    def get():
        pass

    def create():
        pass

    def update():
        pass

    def delete():
        pass

DPUserService = Annotated[UserService, Depends(UserService)]
