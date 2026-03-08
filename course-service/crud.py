import json
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from .models import Course, CourseProgress


def _serialize_course(course: Course):
    return {
        "id": course.id,
        "code": course.code,
        "title": course.title,
        "description": course.description,
        "program": course.program,
        "level": course.level,
        "tags": course.tags,
        "lessons": json.loads(course.lessons or "[]"),
    }


def _serialize_progress(progress: CourseProgress):
    return {
        "id": progress.id,
        "user_id": progress.user_id,
        "course_id": progress.course_id,
        "course_title": progress.course_title,
        "lesson_index": progress.lesson_index,
        "lesson_title": progress.lesson_title,
        "status": progress.status,
        "updated_at": progress.updated_at,
    }


def list_courses(db: Session, program: str | None = None):
    q = db.query(Course)
    if program:
        q = q.filter(Course.program == program)
    items = q.order_by(Course.id.desc()).all()
    return [_serialize_course(item) for item in items]


def get_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        return None
    return _serialize_course(course)


def create_course(db: Session, payload: dict):
    lessons = payload.pop("lessons", [])
    c = Course(
        **payload,
        lessons=json.dumps(lessons, ensure_ascii=False),
    )
    db.add(c)
    db.commit()
    db.refresh(c)
    return _serialize_course(c)


def delete_course(db: Session, course_id: int) -> bool:
    c = db.query(Course).filter(Course.id == course_id).first()
    if not c:
        return False
    db.delete(c)
    db.commit()
    return True

def get_latest_progress(db: Session, user_id: str):
    progress = (
        db.query(CourseProgress)
        .filter(CourseProgress.user_id == user_id)
        .order_by(CourseProgress.updated_at.desc(), CourseProgress.id.desc())
        .first()
    )
    if not progress:
        return None
    return _serialize_progress(progress)

def list_progress_history(db: Session, user_id: str, limit: int = 10):
    items = (
        db.query(CourseProgress)
        .filter(CourseProgress.user_id == user_id)
        .order_by(CourseProgress.updated_at.desc(), CourseProgress.id.desc())
        .limit(limit)
        .all()
    )
    return [_serialize_progress(item) for item in items]


def save_progress(
    db: Session,
    *,
    user_id: str,
    course_id: int,
    lesson_index: int,
    lesson_title: str,
    status: str,
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        return None

    now = datetime.now(timezone.utc).isoformat()

    progress = (
        db.query(CourseProgress)
        .filter(
            CourseProgress.user_id == user_id,
            CourseProgress.course_id == course_id,
        )
        .first()
    )

    if progress:
        progress.lesson_index = lesson_index
        progress.lesson_title = lesson_title
        progress.status = status
        progress.course_title = course.title
        progress.updated_at = now
    else:
        progress = CourseProgress(
            user_id=user_id,
            course_id=course_id,
            course_title=course.title,
            lesson_index=lesson_index,
            lesson_title=lesson_title,
            status=status,
            updated_at=now,
        )
        db.add(progress)

    db.commit()
    db.refresh(progress)
    return _serialize_progress(progress)
