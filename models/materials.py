from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from config.db import Base
import enum

class TipoMaterial(str, enum.Enum):
    """
    Enumerador para los tipos de materiales disponibles.
    """
    CANON = "Cañón"
    COMPUTADORA = "Computadora"
    EXTENSION = "Extensión"

class Estatus(str, enum.Enum):
    """
    Enumerador para los estados posibles de un material.
    """
    DISPONIBLE = "Disponible"
    PRESTADO = "Prestado"
    EN_MANTENIMIENTO = "En Mantenimiento"

class Material(Base):
    """
    Modelo SQLAlchemy para representar materiales en la base de datos.
    """
    __tablename__ = "tbb_materiales"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment="ID único del material")
    tipo_material = Column(Enum(TipoMaterial), nullable=False, comment="Tipo de material (Cañón, Computadora, Extensión)")
    marca = Column(String(50), nullable=False, comment="Marca del material")
    modelo = Column(String(50), nullable=False, comment="Modelo del material")
    estatus = Column(Enum(Estatus), nullable=False, default=Estatus.DISPONIBLE, comment="Estado actual del material")
    fecha_registro = Column(DateTime, default=func.now(), nullable=False, comment="Fecha de creación del registro")
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now(), comment="Fecha de última actualización")

    def __repr__(self):
        """
        Representación legible del objeto Material.
        """
        return f"<Material(id={self.id}, tipo_material={self.tipo_material}, marca={self.marca}, modelo={self.modelo})>"
