from sqlmodel import SQLModel, Field



'''Esta clase permite crear la tabla curso en la base de datos
    id del curso
    nombre del curso
    nombre del profesor que da el curso
    modalidad en la que se da el curso (virtual, presencial)
'''


class Courses(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    name_teacher: str
    course_type:str
    classroom:str
    credits:int

    