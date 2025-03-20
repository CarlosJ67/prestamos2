import models.loans
import schemas.loans
from sqlalchemy.orm import Session

# Obtener todos los préstamos
def get_loans(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de préstamos con paginación.
    :param db: Sesión de la base de datos.
    :param skip: Número de registros a omitir (para paginación).
    :param limit: Número máximo de registros a devolver.
    :return: Lista de préstamos.
    """
    return db.query(models.loans.Loan).offset(skip).limit(limit).all()

# Obtener un préstamo por ID
def get_loan(db: Session, id: int):
    """
    Obtiene un préstamo por su ID.
    :param db: Sesión de la base de datos.
    :param id: ID del préstamo.
    :return: El préstamo encontrado o None si no existe.
    """
    return db.query(models.loans.Loan).filter(models.loans.Loan.id == id).first()

# Crear un nuevo préstamo
def create_loan(db: Session, loan: schemas.loans.LoanCreate):
    """
    Crea un nuevo préstamo en la base de datos.
    :param db: Sesión de la base de datos.
    :param loan: Datos del préstamo a crear.
    :return: El préstamo creado.
    """
    db_loan = models.loans.Loan(
        id_usuario=loan.id_usuario,
        id_material=loan.id_material,
        estatus_prestamo=loan.estatus_prestamo,
        # fecha_prestamo y fecha_devolucion son opcionales y automáticas
    )
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

# Actualizar un préstamo existente
def update_loan(db: Session, id: int, loan_data: schemas.loans.LoanUpdate):
    """
    Actualiza un préstamo existente.
    :param db: Sesión de la base de datos.
    :param id: ID del préstamo a actualizar.
    :param loan_data: Datos actualizados del préstamo.
    :return: El préstamo actualizado o None si no existe.
    """
    db_loan = db.query(models.loans.Loan).filter(models.loans.Loan.id == id).first()
    if db_loan is None:
        return None  # Préstamo no encontrado

    # Actualizar los campos del préstamo
    db_loan.id_usuario = loan_data.id_usuario
    db_loan.id_material = loan_data.id_material
    db_loan.fecha_devolucion = loan_data.fecha_devolucion
    db_loan.estatus_prestamo = loan_data.estatus_prestamo
    # fecha_actualizacion se actualiza automáticamente gracias a `onupdate` en el modelo

    db.commit()
    db.refresh(db_loan)
    return db_loan

# Eliminar un préstamo
def delete_loan(db: Session, id: int):
    """
    Elimina un préstamo por su ID.
    :param db: Sesión de la base de datos.
    :param id: ID del préstamo a eliminar.
    :return: Mensaje de éxito o None si no existe.
    """
    db_loan = db.query(models.loans.Loan).filter(models.loans.Loan.id == id).first()
    if db_loan is None:
        return None  # Préstamo no encontrado

    db.delete(db_loan)
    db.commit()
    return {"message": "Loan deleted successfully"}
