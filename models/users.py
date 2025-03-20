from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from config.db import Base
import enum

class TipoUsuario(str, enum.Enum):
    """
    Enumerador para los tipos de usuarios disponibles.
    """
    ALUMNO = "Alumno"
    PROFESOR = "Profesor"
    SECRETARIA = "Secretaria"
    LABORATORISTA = "Laboratorista"
    DIRECTIVO = "Directivo"
    ADMINISTRATIVO = "Administrativo"

class Estatus(str, enum.Enum):
    """
    Enumerador para los estados posibles de un usuario.
    """
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    BLOQUEADO = "Bloqueado"
    SUSPENDIDO = "Suspendido"

class User(Base):
    """
    Modelo SQLAlchemy para representar usuarios en la base de datos.
    """
    __tablename__ = "tbb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment="ID único del usuario")
    nombre = Column(String(60), nullable=False, comment="Nombre del usuario")
    primer_apellido = Column(String(60), nullable=False, comment="Primer apellido del usuario")
    segundo_apellido = Column(String(60), nullable=True, comment="Segundo apellido del usuario (opcional)")
    tipo_usuario = Column(Enum(TipoUsuario), nullable=False, comment="Tipo de usuario (Alumno, Profesor, etc.)")
    nombre_usuario = Column(String(60), nullable=False, unique=True, comment="Nombre de usuario único")
    correo_electronico = Column(String(100), nullable=False, unique=True, comment="Correo electrónico del usuario")
    contrasena = Column(String(128), nullable=False, comment="Contraseña cifrada del usuario")
    numero_telefono = Column(String(20), nullable=True, comment="Número de teléfono del usuario (opcional)")
    estatus = Column(Enum(Estatus), nullable=False, default=Estatus.ACTIVO, comment="Estado actual del usuario")
    fecha_registro = Column(DateTime, default=func.now(), nullable=False, comment="Fecha de creación del registro")
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now(), comment="Fecha de última actualización")

    def __repr__(self):
        """
        Representación legible del objeto User.
        """
        return f"<User(id={self.id}, nombre={self.nombre}, correo_electronico={self.correo_electronico})>"
