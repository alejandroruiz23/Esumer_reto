from fastapi import FastAPI

from database.db import create_all_tables


app = FastAPI()

@app.get("/")
def saludo():
    return {"saludo":"hola"}


