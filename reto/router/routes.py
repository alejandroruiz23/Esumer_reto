from fastapi import APIRouter

# from controllers.auth_controller import route as AuthRoute
from controllers.user_controller import route as UserRoute
from controllers.category_controller import route as CategoryRoute

routes = APIRouter()

routes.include_router(UserRoute, prefix="/users", tags=["Users"])
routes.include_router(AuthRoute, prefix="/auth", tags=["Auth"])
routes.include_router(CategoryRoute, prefix="/category", tags=["Category"])