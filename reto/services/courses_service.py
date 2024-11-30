from typing import Annotated
from fastapi import Depends, HTTPException, status

from sqlmodel import select

from database.db import DBSession
from models.entities.courses import Courses
from models.schemas.courses import CoursesCreate, CoursesRead, CourseUpdate

class CoursesService:
    def __init__(self, db: DBSession) -> None:
        self.db = db
        

    def get_all(self):
        courses = self.db.exec(select(Courses)).all()
        return courses


    def get_by_id(self, id: int):
        course = self.db.get(Courses, id)

        if course == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")

        return course

    def create(self,course_data:CoursesCreate):
        course = Courses.model_validate(course_data.model_dump())
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)

        return course

    def update(self,id:int ,course_data:CourseUpdate):
        course_db = self.db.get(Courses, id)
        if course_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")
        
        course_db_dict= course_data.model_dump(exclude_unset=True)
        course_db.sqlmodel_update(course_db_dict)
        self.db.add(course_db)
        self.db.commit()
        self.db.refresh(course_db)
        return course_db


    def delete_course(self, id:int):
        course_db = self.db.get(Courses, id)

        if course_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")
        self.db.delete(course_db)
        self.db.commit()
        return{"detail":"Curso eliminado"}

DPCourseService = Annotated[CoursesService, Depends(CoursesService)]