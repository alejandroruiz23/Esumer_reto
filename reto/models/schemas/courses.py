from sqlmodel import SQLModel

class CoursesCreate(SQLModel):
    name:str
    name_teacher:str
    course_type:str
    classroom:str
    credits:int

class CoursesRead(SQLModel):
    id: int
    name: str
    name_teacher: str
    course_type:str
    classroom:str
    credits:int

class CourseUpdate(CoursesCreate):
    pass