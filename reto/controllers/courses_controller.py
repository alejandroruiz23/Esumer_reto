from fastapi import APIRouter

from models.schemas.courses import CoursesCreate, CoursesRead, CourseUpdate
from services.courses_service import DPCourseService


route = APIRouter()

@route.get("/", response_model=list[CoursesRead])
async def get_all(course_service: DPCourseService):
    course_db = course_service.get_all()
    return course_db

@route.get("/{id}", response_model=CoursesRead)
async def get_by_id(id: int, course_service: DPCourseService):
    course_db = course_service.get_by_id(id)
    return course_db

@route.post("/", response_model=CoursesCreate)
def create(course_data:CoursesCreate,course_service: DPCourseService):
    category = course_service.create(course_data)
    return category

@route.put("/{id}", response_model=CoursesRead)
def update(course_data: CourseUpdate, id:int, course_service: DPCourseService):
    course_update = course_service.update(id,course_data)
    return course_update

@route.delete("/{id}")
def delete(id:int,course_service: DPCourseService):
    return course_service.delete_course(id)