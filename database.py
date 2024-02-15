from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL (replace with your PostgreSQL database URL)
DATABASE_URL = "postgresql://postgres:Arif@localhost/todo_db"

# Create a SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker to manage database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()