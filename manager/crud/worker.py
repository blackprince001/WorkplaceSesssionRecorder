from manager.schema.worker import WorkerCreate
from manager.models import Worker as WorkerModel
from sqlalchemy.orm import Session
from sqlalchemy import select


def create_worker(db: Session, worker: WorkerCreate) -> WorkerModel:
    db_worker = WorkerModel(**worker.dict())

    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)

    return db_worker


def get_worker(db: Session, name: str) -> WorkerModel:
    return db.scalar(select(WorkerModel).where(WorkerModel.name == name))
