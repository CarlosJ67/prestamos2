from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class LoanBase(BaseModel):
    """
    Esquema base para los préstamos.
    """
    id_usuario: int
    id_material: int
    fecha_prestamo: Optional[datetime] = None  # Opcional
    fecha_devolucion: Optional[datetime] = None  # Opcional
    estatus_prestamo: str

class LoanCreate(LoanBase):
    """
    Esquema para crear un nuevo préstamo.
    """
    pass

class LoanUpdate(LoanBase):
    """
    Esquema para actualizar un préstamo existente.
    """
    pass

class Loan(LoanBase):
    """
    Esquema para representar un préstamo completo (incluyendo su ID).
    """
    id: int

    class Config:
        from_attributes = True  # Cambio de orm_mode a from_attributes (Pydantic v2)
