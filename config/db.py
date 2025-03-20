import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Construir la URL de conexión a la base de datos utilizando las variables de entorno
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Crear el motor de la base de datos sin configuración SSL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una fábrica de sesiones locales
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos SQLAlchemy
Base = declarative_base()

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()