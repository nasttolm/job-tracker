from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import get_db
from auth import get_current_user

# Create a router for vacancy-related endpoints
router = APIRouter(
    prefix="/vacancies",  # All routes will start with /vacancies
    tags=["Vacancies"]    # Tag for Swagger UI grouping
)

@router.post("/", response_model=schemas.VacancyOut, status_code=status.HTTP_201_CREATED)
def create_vacancy(
    vacancy: schemas.VacancyCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)):
    
    """
    Create a new vacancy and link it to the current user.
    """
    new_vacancy = models.Vacancy(user_id=current_user.id, **vacancy.dict())
    db.add(new_vacancy)
    db.commit()
    db.refresh(new_vacancy)
    return new_vacancy


@router.get("/", response_model=List[schemas.VacancyOut])
def get_user_vacancies(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Get all vacancies created by the currently authenticated user.
    """
    vacancies = db.query(models.Vacancy).filter(models.Vacancy.user_id == current_user.id).all()
    return vacancies

@router.get("/{vacancy_id}", response_model=schemas.VacancyOut)
def get_vacancy_by_id(
    vacancy_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Get a single vacancy by its ID if it belongs to the current user.
    """
    vacancy = db.query(models.Vacancy).filter(
        models.Vacancy.id == vacancy_id,
        models.Vacancy.user_id == current_user.id
    ).first()

    if not vacancy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy not found")
    
    return vacancy

@router.delete("/{vacancy_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vacancy(
    vacancy_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Delete a vacancy by its ID if it belongs to the current user.
    """
    vacancy = db.query(models.Vacancy).filter(
        models.Vacancy.id == vacancy_id,
        models.Vacancy.user_id == current_user.id
    ).first()

    if not vacancy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy not found")

    db.delete(vacancy)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{vacancy_id}", response_model=schemas.VacancyOut)
def update_vacancy(
    vacancy_id: int,
    updated_data: schemas.VacancyCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Update an existing vacancy if it belongs to the current user.
    """
    vacancy = db.query(models.Vacancy).filter(
        models.Vacancy.id == vacancy_id,
        models.Vacancy.user_id == current_user.id
    ).first()

    if not vacancy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy not found")

    for key, value in updated_data.dict().items():
        setattr(vacancy, key, value)

    db.commit()
    db.refresh(vacancy)
    return vacancy