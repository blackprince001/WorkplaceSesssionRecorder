from sqlalchemy.orm import Session
from sqlalchemy import select
from manager.schema.checkbook import CheckBookCreate
from manager.models import CheckBook as CheckBookModel


def create_checkin(db: Session, checkin: CheckBookCreate) -> CheckBookModel:
    db_checkin = CheckBookModel(**checkin.dict())

    db.add(db_checkin)
    db.commit()
    db.refresh(db_checkin)

    return db_checkin


def get_checkin(db: Session, name: str) -> CheckBookModel:
    return db.scalar(select(CheckBookModel).where(CheckBookModel.name == name))
