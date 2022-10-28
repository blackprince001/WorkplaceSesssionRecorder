from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

BASE = declarative_base()

# TODO add more columns to the Worker Table
class Worker(BASE):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)


class CheckBook(BASE):
    __tablename__ = "checkbook"

    name = Column(String, primary_key=True)
    checkin_start = Column(DateTime, nullable=False)
    checkin_end = Column(DateTime, nullable=False)

# TODO create a relational data Table to Worker