from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum, func
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class EstatusPrestamo(str, enum.Enum):
    """
    Enumerador para los estados posibles de un préstamo.
    """
    ACTIVO = "Activo"
    DEVUELTO = "Devuelto"
    VENCIDO = "Vencido"

class Loan(Base):
    """
    Modelo SQLAlchemy para representar préstamos en la base de datos.
    """
    __tablename__ = "tbb_prestamos"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment="ID único del préstamo")
    id_usuario = Column(Integer, ForeignKey("tbb_usuarios.id"), nullable=False, comment="ID del usuario que realiza el préstamo")
    id_material = Column(Integer, ForeignKey("tbb_materiales.id"), nullable=False, comment="ID del material prestado")
    fecha_prestamo = Column(DateTime, default=func.now(), nullable=False, comment="Fecha en que se realizó el préstamo")
    fecha_devolucion = Column(DateTime, nullable=True, comment="Fecha en que se devolvió el material (opcional)")
    estatus_prestamo = Column(Enum(EstatusPrestamo), nullable=False, default=EstatusPrestamo.ACTIVO, comment="Estado actual del préstamo")

    # Relaciones
    usuario = relationship("User", backref="prestamos")
    material = relationship("Material", backref="prestamos")

    def __repr__(self):
        """
        Representación legible del objeto Loan.
        """
        return f"<Loan(id={self.id}, id_usuario={self.id_usuario}, id_material={self.id_material}, estatus_prestamo={self.estatus_prestamo})>"
