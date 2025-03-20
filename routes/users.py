from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from config.db import get_db
from schemas.users import UserLogin, User, UserCreate, UserUpdate
from crud.users import (
    authenticate_user,
    get_users as get_users_db,
    get_user as get_user_db,
    create_user as create_user_db,
    update_user as update_user_db,
    delete_user as delete_user_db
)
from config.jwt import create_access_token, get_current_user

# Inicializamos el enrutador de usuarios
user = APIRouter()
security = HTTPBearer()

# ✅ Endpoint de autenticación
@user.post("/login", response_model=dict, tags=["Autenticación"])
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(
        db, username=user_data.username, email=user_data.email, phone=user_data.phone, password=user_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.nombre_usuario}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

# ✅ Ruta protegida (ver usuario autenticado)
@user.get("/protected", response_model=User, tags=["Autenticación"])
async def protected_route(current_user: User = Depends(get_current_user)):
    return current_user

# ✅ Obtener todos los usuarios (protegido)
@user.get("/users", response_model=list[User], tags=["Usuarios"])
async def read_users(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return get_users_db(db=db, skip=skip, limit=limit)

# ✅ Obtener un usuario por ID (protegido)
@user.get("/users/{id}", response_model=User, tags=["Usuarios"])
async def read_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_user = get_user_db(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# ✅ Crear un nuevo usuario (SIN PROTECCIÓN)
@user.post("/users", response_model=User, tags=["Usuarios"])
async def create_new_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user_db(db=db, user=user_data)

# ✅ Actualizar un usuario existente (protegido)
@user.put("/users/{id}", response_model=User, tags=["Usuarios"])
async def update_user_route(
    id: int, user_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    db_user = update_user_db(db=db, id=id, user_data=user_data)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# ✅ Eliminar un usuario (protegido)
@user.delete("/users/{id}", response_model=dict, tags=["Usuarios"])
async def delete_user_route(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = delete_user_db(db=db, id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return result