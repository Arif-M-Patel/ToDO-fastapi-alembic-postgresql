from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL 
DATABASE_URL = "postgresql://postgres:Arif@localhost/todo_db"

# database engine
engine = create_engine(DATABASE_URL)

#  sessionmaker to manage database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
