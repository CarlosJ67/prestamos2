from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.loans
import config.db
import schemas.loans
from typing import List
from config.jwt import get_current_user  # Importa get_current_user
from schemas.users import User  # Importa el modelo de usuario

# Crear un router para los préstamos
loan = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los préstamos (protegido)
@loan.get("/loans", response_model=List[schemas.loans.Loan], tags=["Préstamos"])
async def read_loans(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Protege la ruta
):
    """
    Obtiene una lista de préstamos con paginación.
    """
    db_loans = crud.loans.get_loans(db=db, skip=skip, limit=limit)
    return db_loans

# Obtener un préstamo por ID (protegido)
@loan.get("/loans/{id}", response_model=schemas.loans.Loan, tags=["Préstamos"])
async def read_loan(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Protege la ruta
):
    """
    Obtiene un préstamo por su ID.
    """
    db_loan = crud.loans.get_loan(db=db, id=id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan

# Crear un nuevo préstamo (protegido)
@loan.post("/loans", response_model=schemas.loans.Loan, tags=["Préstamos"])
async def create_loan(
    loan_data: schemas.loans.LoanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Protege la ruta
):
    """
    Crea un nuevo préstamo.
    """
    return crud.loans.create_loan(db=db, loan=loan_data)

# Actualizar un préstamo existente (protegido)
@loan.put("/loans/{id}", response_model=schemas.loans.Loan, tags=["Préstamos"])
async def update_loan(
    id: int,
    loan_data: schemas.loans.LoanUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Protege la ruta
):
    """
    Actualiza un préstamo existente.
    """
    db_loan = crud.loans.update_loan(db=db, id=id, loan_data=loan_data)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan

# Eliminar un préstamo (protegido)
@loan.delete("/loans/{id}", response_model=dict, tags=["Préstamos"])
async def delete_loan(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Protege la ruta
):
    """
    Elimina un préstamo por su ID.
    """
    result = crud.loans.delete_loan(db=db, id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return result
