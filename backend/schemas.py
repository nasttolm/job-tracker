from datetime import datetime
from pydantic import BaseModel, EmailStr

# Schema for creating a new user (input)
class UserCreate(BaseModel):
    email: EmailStr  # The user's email address (validated format)
    password: str    # The user's password as plain text

# Schema for returning user data (output)
class UserOut(BaseModel):
    id: int  # The unique ID of the user
    email: EmailStr  # The user's email address
    date_created: datetime  # Timestamp when the user was created

    class Config:
        orm_mode = True  # Enables compatibility with ORM objects like SQLAlchemy models

# Schema for login request
class UserLogin(BaseModel):
    email: EmailStr  # The user's email address
    password: str    # The user's password


# Schema for creating a new vacancy (input)
class VacancyCreate(BaseModel):
    title: str  # Job title
    company: str  # Company name
    status: str = "applied"  # Application status, default is "applied"

# Schema for returning vacancy data (output)
class VacancyOut(BaseModel):
    id: int  # The unique ID of the vacancy
    title: str  # Job title
    company: str  # Company name
    status: str  # Current application status
    date_created: datetime  # Timestamp when the vacancy was created
    user_id: int  # ID of the user who created the vacancy (useful for admin views)

    class Config:
        orm_mode = True  # Enables compatibility with ORM objects like SQLAlchemy models