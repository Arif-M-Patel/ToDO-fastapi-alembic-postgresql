from pydantic import BaseModel


class TodoBase(BaseModel):
    # id: int
    title: str
    description: str = None
    


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    completed: bool
    id: int
    # title: str
    # description: str = None
    

    class Config:
        orm_mode = True
