from sqlalchemy.orm import Session

from app.core.logger import logger
from app.services.parser import process_csv
from app.services.repository import insert_or_update_product, delete_missing_products


def sync_products(db: Session, file_path):
    new_products = process_csv(file_path)
    existing_ids = set()
    for product in new_products:
        insert_or_update_product(db, product)
        existing_ids.add(product.id)
    try:
        delete_missing_products(db, existing_ids)
    except Exception as e:
        logger.error(f"Error al eliminar producto: {e}")
        db.rollback()
        raise
    logger.info("Sincronización completada.")
