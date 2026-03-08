from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from shared.database import Base


class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(50), index=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text, default="")
    program: Mapped[str] = mapped_column(String(20), index=True)  # BSCS/BSIT/BSIS/BTVTED
    level: Mapped[str] = mapped_column(String(50), default="")
    tags: Mapped[str] = mapped_column(Text, default="")
    lessons: Mapped[str] = mapped_column(Text, default="[]")


class CourseProgress(Base):
    __tablename__ = "course_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(100), index=True)
    course_id: Mapped[int] = mapped_column(Integer, index=True)
    course_title: Mapped[str] = mapped_column(String(255), default="")
    lesson_index: Mapped[int] = mapped_column(Integer, default=0)
    lesson_title: Mapped[str] = mapped_column(String(255), default="")
    status: Mapped[str] = mapped_column(String(50), default="in_progress")
    updated_at: Mapped[str] = mapped_column(String(50), default="")