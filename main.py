from fastapi import  FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import List
import models, schemas, database
from database import SessionLocal, engine

# Create a FastAPI app instance
app = FastAPI(debug=True, title="ToDo list")


models.Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to get a single Todo item by ID
def get_todo_by_id(db: Session, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo

# Function to get all Todo items
def get_all_todos(db: Session):
    return db.query(models.Todo).all()

# Function to create a new Todo item
def create_todo_list(db, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# Function to update the completion status of a Todo item
def update_todo_completion(db: Session, todo_id: int, completed: bool):
    todo = get_todo_by_id(db, todo_id)
    todo.completed = completed
    db.commit()
    return todo

# Function to delete a single Todo item by ID
def delete_todo_by_id(db: Session, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    db.delete(todo)
    db.commit()
    return {"message": f"Todo item with ID {todo_id} deleted successfully"}


#Welcome
@app.get("/")
async def welcome():
    return {"detail": "welcome To My ToDO List"}

# route to create a new Todo item
@app.post("/todos/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return create_todo_list (db, todo)

# route to retrieve a single Todo item by ID
@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    return get_todo_by_id(db, todo_id)

# route to retrieve all Todo items
@app.get("/todos/", response_model=List[schemas.Todo])
def read_all_todos(db: Session = Depends(get_db)):
    return get_all_todos(db)

# route to update the completion status of a Todo item
@app.put("/todos/{todo_id}/review", response_model=schemas.Todo)
def review_todo(todo_id: int, completed: bool, db: Session = Depends(get_db)):
    return update_todo_completion(db, todo_id, completed)

# route to delete a single Todo item by ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo_by_id(db, todo_id)


