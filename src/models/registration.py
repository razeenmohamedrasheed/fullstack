from pydantic import BaseModel


class Registration(BaseModel):
    username: str
    email: str
    contact: str
    password: str
    course_id: int
    user_role: int
