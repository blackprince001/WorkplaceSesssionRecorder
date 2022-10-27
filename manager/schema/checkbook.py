from pydantic import BaseModel
from datetime import datetime


class CheckBookBase(BaseModel):
    pass


class CheckBookCreate(CheckBookBase):
    name: str
    checkin_start: datetime
    checkin_end: datetime


class CheckBook(CheckBookBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
