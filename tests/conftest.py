import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from manager.models import BASE
from manager.schema.checkbook import CheckBookCreate
from manager.schema.worker import WorkerCreate


@pytest.fixture(scope="session")
def engine():
    return create_engine(url="sqlite+pysqlite:///:memory:", future=True)


@pytest.fixture(scope="session")
def worker():
    return WorkerCreate(name="blackprince")


@pytest.fixture(scope="session")
def checkbook():
    _start = datetime.datetime.now()
    _end = datetime.datetime.now() + datetime.timedelta(hours=2, seconds=30)
    
    return CheckBookCreate(
        name="blackprince",
        checkin_start=_start,
        checkin_end=_end,
    )


@pytest.fixture
def db():
    with Session(engine) as session:
        BASE.metadata.create_all(bind=engine)
        yield session
