from typing import List
from pydantic import BaseModel, Field, ConfigDict


class LessonItem(BaseModel):
    title: str
    content: str


class CourseIn(BaseModel):
    code: str
    title: str
    description: str = ""
    program: str = Field(pattern="^(BSCS|BSIT|BSIS|BTVTED)$")
    level: str = ""
    tags: str = ""
    lessons: List[LessonItem] = Field(default_factory=list)


class CourseOut(CourseIn):
    id: int
    model_config = ConfigDict(from_attributes=True)


class CourseProgressIn(BaseModel):
    course_id: int
    lesson_index: int = 0
    lesson_title: str = ""
    status: str = Field(default="in_progress", pattern="^(in_progress|completed)$")


class CourseProgressOut(BaseModel):
    id: int
    user_id: str
    course_id: int
    course_title: str
    lesson_index: int
    lesson_title: str
    status: str
    updated_at: str
    model_config = ConfigDict(from_attributes=True)