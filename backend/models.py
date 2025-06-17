from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base

# User model represents a user in the system
class User(Base):
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique user ID
    email = Column(String, unique=True, index=True, nullable=False)  # User's email
    hashed_password = Column(String, nullable=False)  # Encrypted password
    date_created = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp when the user was created
    
    # Relationship to link users to their vacancies
    vacancies = relationship("Vacancy", back_populates="owner")


# Vacancy model represents a job application created by a user
class Vacancy(Base):
    __tablename__ = "vacancies"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique vacancy ID
    title = Column(String, nullable=False)  # Job title
    company = Column(String, nullable=False)  # Company name
    status = Column(String, default="applied")  # Status of the application
    date_applied = Column(DateTime(timezone=True), server_default=func.now())  # Date the application was made
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign key to the User who created this vacancy

    # Relationship to link each vacancy to its owner
    owner = relationship("User", back_populates="vacancies")