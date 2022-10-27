from pydantic import BaseModel


class WorkerBase(BaseModel):
    pass


class WorkerCreate(WorkerBase):
    name: str


class Worker(WorkerBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
