from fastapi import APIRouter, Depends, FastAPI
import schemas
from auth import get_current_user
from database import Base, engine

from models import User
from routers import users, vacancies


# Create an instance of the FastAPI application
app = FastAPI()

# Connect routes from users.py
app.include_router(users.router)

# Connect routes from vacancies.py
app.include_router(vacancies.router)

# Create all tables in the database (based on models that will be defined later)
# This is a one-time action during startup to ensure tables exist
Base.metadata.create_all(bind=engine)

# Define a route at the root URL "/"
@app.get("/")
def root():
    # When this route is accessed with GET request, return a JSON message
    return {"message": "Job Tracker API is running"}

@app.get("/me", response_model=schemas.UserOut)
def read_current_user(current_user: schemas.UserOut = Depends(get_current_user)):
    # This route is protected. It returns the current logged-in user.
    return current_user


