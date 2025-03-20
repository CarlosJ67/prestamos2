from sqlalchemy.orm import Session
from models.users import User, TipoUsuario, Estatus as UserEstatus
from models.materials import Material, TipoMaterial, Estatus as MaterialEstatus
from models.loans import Loan, EstatusPrestamo
from config.db import engine, SessionLocal
from passlib.context import CryptContext

# Configuración para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

# Datos de prueba para usuarios
users_data = [
    {
        "nombre": "Juan",
        "primer_apellido": "Pérez",
        "segundo_apellido": "Gómez",
        "tipo_usuario": TipoUsuario.ALUMNO,
        "nombre_usuario": "juanperez",
        "correo_electronico": "juan.perez@example.com",
        "contrasena": get_password_hash("password123"),
        "numero_telefono": "5551234567",
        "estatus": UserEstatus.ACTIVO,
    },
    {
        "nombre": "María",
        "primer_apellido": "López",
        "segundo_apellido": "Martínez",
        "tipo_usuario": TipoUsuario.PROFESOR,
        "nombre_usuario": "marialopez",
        "correo_electronico": "maria.lopez@example.com",
        "contrasena": get_password_hash("password123"),
        "numero_telefono": "5557654321",
        "estatus": UserEstatus.ACTIVO,
    },
]

# Datos de prueba para materiales
materials_data = [
    {
        "tipo_material": TipoMaterial.CANON,
        "marca": "Epson",
        "modelo": "PowerLite 1781W",
        "estatus": MaterialEstatus.DISPONIBLE,
    },
    {
        "tipo_material": TipoMaterial.COMPUTADORA,
        "marca": "Dell",
        "modelo": "Latitude 3420",
        "estatus": MaterialEstatus.DISPONIBLE,
    },
    {
        "tipo_material": TipoMaterial.EXTENSION,
        "marca": "APC",
        "modelo": "SurgeArrest P11VNT3",
        "estatus": MaterialEstatus.DISPONIBLE,
    },
]

def seed_database():
    db = SessionLocal()
    try:
        print("Eliminando datos existentes...")
        db.query(Loan).delete()
        db.query(Material).delete()
        db.query(User).delete()
        db.commit()

        print("Insertando nuevos datos...")
        inserted_users = []
        for user_data in users_data:
            user = User(**user_data)
            db.add(user)
            db.commit()
            db.refresh(user)
            inserted_users.append(user)

        inserted_materials = []
        for material_data in materials_data:
            material = Material(**material_data)
            db.add(material)
            db.commit()
            db.refresh(material)
            inserted_materials.append(material)

        loans_data = [
            {
                "id_usuario": inserted_users[0].id,
                "id_material": inserted_materials[0].id,
                "estatus_prestamo": EstatusPrestamo.ACTIVO,
            },
            {
                "id_usuario": inserted_users[1].id,
                "id_material": inserted_materials[1].id,
                "estatus_prestamo": EstatusPrestamo.ACTIVO,
            },
        ]

        db.add_all([Loan(**loan_data) for loan_data in loans_data])
        db.commit()

        print("Datos de prueba insertados correctamente.")
    except Exception as e:
        db.rollback()
        print(f"Error al insertar datos de prueba: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()

