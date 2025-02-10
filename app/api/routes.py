import shutil

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger
from app.services.parser import process_csv
from app.services.repository import insert_or_update_product, get_all_products
from app.services.sync import sync_products


router = APIRouter()

@router.post("/products/")
def insert_products_route(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    logger.info("Iniciando inserción de productos desde CSV.")
    products = process_csv(file_path)
    for product in products:
        insert_or_update_product(db, product)
    return {"message": "Productos insertados o actualizados."}

@router.get("/products/")
def get_products_route(db: Session = Depends(get_db)):
    logger.info("Solicitud para obtener todos los productos.")
    return get_all_products(db)

@router.post("/sync/")
def sync_products_route(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    logger.info("Iniciando sincronización con portal externo.")
    sync_products(db, file_path)
    return {"message": "Sincronización completada."}
