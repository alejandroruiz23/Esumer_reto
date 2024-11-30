from fastapi import APIRouter

from controllers.auth_controller import route as AuthRoute
from controllers.user_controller import route as UserRoute

routes = APIRouter()

routes.include_router(AuthRoute, prefix="/users", tags=["Users"])
routes.include_router(UserRoute, prefix="/auth", tags=["Auth"])