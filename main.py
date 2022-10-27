from manager.core import engine
from manager.models import BASE
from sqlalchemy.orm import Session
from manager.schema.worker import WorkerCreate
from manager.schema.checkbook import CheckBookCreate
from manager.crud.worker import create_worker, get_worker
from manager.crud.checker import create_checkin, get_checkin
import datetime

BASE.metadata.create_all(bind=engine)


def get_db():
    with Session(engine, autoflush=False, autocommit=False) as session:
        return session


def session_length(db: Session, checkin_name: str) -> None:
    session_point = get_checkin(db=db, name=get_worker(db=db, name="prince").name)  # type: ignore
    session_len = session_point.checkin_end - session_point.checkin_start

    print(session_len)


if __name__ == "__main__":
    db = get_db()
    workers = ["prince", "jason", "mark", "kevin"]

    for worker in workers:
        create_worker(db=db, worker=WorkerCreate(name=worker))

    start = datetime.datetime.now()

    while True:
        p_quit = input("Press Q to quit: ")
        if p_quit == "q":
            end = datetime.datetime.now()

            create_checkin(
                db=db,
                checkin=CheckBookCreate(
                    name=get_worker(db=db, name="prince").name, # type: ignore
                    checkin_start=start,
                    checkin_end=end,
                ),
            )
            break
