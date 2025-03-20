from typing import Optional  # Importar Optional
from passlib.context import CryptContext
from sqlalchemy.orm import Session  # Importar Session
import models.users
import schemas.users

# Configuración para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para verificar contraseñas
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Función para autenticar usuarios
def authenticate_user(db: Session, password: str, username: Optional[str] = None, email: Optional[str] = None, phone: Optional[str] = None):
    if username:
        user = db.query(models.users.User).filter(models.users.User.nombre_usuario == username).first()
    elif email:
        user = db.query(models.users.User).filter(models.users.User.correo_electronico == email).first()
    elif phone:
        user = db.query(models.users.User).filter(models.users.User.numero_telefono == phone).first()
    else:
        return None

    if not user or not verify_password(password, user.contrasena):
        return None
    return user

# Función para obtener un usuario por nombre de usuario
def get_user_by_username(db: Session, username: str):
    return db.query(models.users.User).filter(models.users.User.nombre_usuario == username).first()

# Obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

# Obtener un usuario por ID
def get_user(db: Session, id: int):
    return db.query(models.users.User).filter(models.users.User.id == id).first()

# Crear un nuevo usuario
def create_user(db: Session, user: schemas.users.UserCreate):
    hashed_password = pwd_context.hash(user.contrasena)
    db_user = models.users.User(
        nombre=user.nombre,
        primer_apellido=user.primer_apellido,
        segundo_apellido=user.segundo_apellido,
        tipo_usuario=user.tipo_usuario,
        nombre_usuario=user.nombre_usuario,
        correo_electronico=user.correo_electronico,
        contrasena=hashed_password,
        numero_telefono=user.numero_telefono,
        estatus=user.estatus,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Actualizar un usuario existente
def update_user(db: Session, id: int, user_data: schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user is None:
        return None

    db_user.nombre = user_data.nombre
    db_user.primer_apellido = user_data.primer_apellido
    db_user.segundo_apellido = user_data.segundo_apellido
    db_user.tipo_usuario = user_data.tipo_usuario
    db_user.nombre_usuario = user_data.nombre_usuario
    db_user.correo_electronico = user_data.correo_electronico
    db_user.numero_telefono = user_data.numero_telefono
    db_user.estatus = user_data.estatus

    if user_data.contrasena:
        db_user.contrasena = pwd_context.hash(user_data.contrasena)

    db.commit()
    db.refresh(db_user)
    return db_user

# Eliminar un usuario
def delete_user(db: Session, id: int):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")  # ✅ Manejar correctamente

    db.delete(db_user)
    db.commit()

    return {"message": f"Usuario con ID {id} eliminado correctamente"}  # ✅ Retornar JSON válido