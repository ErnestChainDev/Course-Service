from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session

from shared.database import db_dependency
from .schemas import (
    CourseIn,
    CourseOut,
    CourseProgressIn,
    CourseProgressOut,
)
from .crud import (
    list_courses,
    get_course,
    create_course,
    delete_course,
    save_progress,
    get_latest_progress,
)


def build_router(SessionLocal):
    router = APIRouter()
    get_db = db_dependency(SessionLocal)

    @router.get("/", response_model=list[CourseOut])
    def get_all(
        program: str | None = Query(default=None),
        db: Session = Depends(get_db),
    ):
        return list_courses(db, program)

    @router.post("/", response_model=CourseOut)
    def create(payload: CourseIn, db: Session = Depends(get_db)):
        return create_course(db, payload.model_dump())

    @router.post("/progress", response_model=CourseProgressOut)
    def update_progress(
        payload: CourseProgressIn,
        request: Request,
        db: Session = Depends(get_db),
    ):
        user_id = (request.headers.get("X-User-ID") or "").strip()
        if not user_id:
            raise HTTPException(status_code=401, detail="Missing X-User-ID header")

        result = save_progress(
            db,
            user_id=user_id,
            course_id=payload.course_id,
            lesson_index=payload.lesson_index,
            lesson_title=payload.lesson_title,
            status=payload.status,
        )
        if not result:
            raise HTTPException(status_code=404, detail="Course not found")
        return result

    @router.get("/progress/latest", response_model=CourseProgressOut)
    def latest_progress(
        request: Request,
        db: Session = Depends(get_db),
    ):
        user_id = (request.headers.get("X-User-ID") or "").strip()
        if not user_id:
            raise HTTPException(status_code=401, detail="Missing X-User-ID header")

        result = get_latest_progress(db, user_id)
        if not result:
            raise HTTPException(status_code=404, detail="No progress found")
        return result

    @router.get("/{course_id}", response_model=CourseOut)
    def get_one(course_id: int, db: Session = Depends(get_db)):
        c = get_course(db, course_id)
        if not c:
            raise HTTPException(status_code=404, detail="Course not found")
        return c

    @router.delete("/{course_id}", response_model=dict)
    def remove(course_id: int, db: Session = Depends(get_db)):
        ok = delete_course(db, course_id)
        if not ok:
            raise HTTPException(status_code=404, detail="Course not found")
        return {"deleted": True}

    return router