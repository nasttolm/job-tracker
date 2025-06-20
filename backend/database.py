from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()  # Loading variables from .env

# URL for connecting to the PostgreSQL database
DATABASE_URL = config("DATABASE_URL")

# Create a SQLAlchemy engine that manages the database connection
# This is the core interface to the database
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class to handle sessions with the database
# SessionLocal will be used to create session instances for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for your ORM models to inherit from
# All models will extend this class to get ORM functionality
Base = declarative_base()


# Dependency to get a database session
# This function ensures the session is opened and closed correctly
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
