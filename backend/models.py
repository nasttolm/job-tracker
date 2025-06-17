from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

# User model represents a user in the system
class User(Base):
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique user ID
    email = Column(String, unique=True, index=True, nullable=False)  # User's email
    hashed_password = Column(String, nullable=False)  # Encrypted password
    date_created = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp when the user was created
