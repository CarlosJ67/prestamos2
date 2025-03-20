import models.materials
import schemas.materials
from sqlalchemy.orm import Session

# Obtener todos los materiales
def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de materiales con paginación.
    :param db: Sesión de la base de datos.
    :param skip: Número de registros a omitir (para paginación).
    :param limit: Número máximo de registros a devolver.
    :return: Lista de materiales.
    """
    return db.query(models.materials.Material).offset(skip).limit(limit).all()

# Obtener un material por ID
def get_material(db: Session, id: int):
    """
    Obtiene un material por su ID.
    :param db: Sesión de la base de datos.
    :param id: ID del material.
    :return: El material encontrado o None si no existe.
    """
    return db.query(models.materials.Material).filter(models.materials.Material.id == id).first()

# Crear un nuevo material
def create_material(db: Session, material: schemas.materials.MaterialCreate):
    """
    Crea un nuevo material en la base de datos.
    :param db: Sesión de la base de datos.
    :param material: Datos del material a crear.
    :return: El material creado.
    """
    db_material = models.materials.Material(
        tipo_material=material.tipo_material,
        marca=material.marca,
        modelo=material.modelo,
        estatus=material.estatus,
        # fecha_registro y fecha_actualizacion son automáticas
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

# Actualizar un material existente
def update_material(db: Session, id: int, material_data: schemas.materials.MaterialUpdate):
    """
    Actualiza un material existente.
    :param db: Sesión de la base de datos.
    :param id: ID del material a actualizar.
    :param material_data: Datos actualizados del material.
    :return: El material actualizado o None si no existe.
    """
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material is None:
        return None  # Material no encontrado

    # Actualizar los campos del material
    db_material.tipo_material = material_data.tipo_material
    db_material.marca = material_data.marca
    db_material.modelo = material_data.modelo
    db_material.estatus = material_data.estatus
    # fecha_actualizacion se actualiza automáticamente gracias a `onupdate` en el modelo

    db.commit()
    db.refresh(db_material)
    return db_material

# Eliminar un material
def delete_material(db: Session, id: int):
    """
    Elimina un material por su ID.
    :param db: Sesión de la base de datos.
    :param id: ID del material a eliminar.
    :return: Mensaje de éxito o None si no existe.
    """
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material is None:
        return None  # Material no encontrado

    db.delete(db_material)
    db.commit()
    return {"message": "Material deleted successfully"}
