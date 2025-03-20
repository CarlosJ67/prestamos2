from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class MaterialBase(BaseModel):
    """
    Esquema base para los materiales.
    """
    tipo_material: str
    marca: str
    modelo: str
    estatus: str
    fecha_registro: Optional[datetime] = None  # Opcional
    fecha_actualizacion: Optional[datetime] = None  # Opcional

class MaterialCreate(MaterialBase):
    """
    Esquema para crear un nuevo material.
    """
    pass

class MaterialUpdate(MaterialBase):
    """
    Esquema para actualizar un material existente.
    """
    pass

class Material(MaterialBase):
    """
    Esquema para representar un material completo (incluyendo su ID).
    """
    id: int

    class Config:
        from_attributes = True  # Cambio de orm_mode a from_attributes (Pydantic v2)
