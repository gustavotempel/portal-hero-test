from core.logger import logger
from services.parser import process_csv
from services.repository import insert_or_update_product, delete_missing_products
from sqlalchemy.orm import Session


def sync_products(db: Session, file_path):
    new_products = process_csv(file_path)
    existing_ids = set()
    for product in new_products:
        insert_or_update_product(db, product)
        existing_ids.add(product.id)
    delete_missing_products(db, existing_ids)
    logger.info("Sincronización completada.")
