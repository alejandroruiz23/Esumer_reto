from typing import Annotated
from fastapi import Depends

from database.db import DBSession

class AuthService:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    async def sign_up():
        pass

    async def login():
        pass

    async def logout():
        pass
