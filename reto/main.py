from fastapi import FastAPI

from database.db import create_all_tables

from router.routes import routes

app = FastAPI(lifespan=create_all_tables)

app.include_router(routes, prefix="/api")


