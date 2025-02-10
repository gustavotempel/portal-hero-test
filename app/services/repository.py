from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.product import Product


def insert_or_update_product(db: Session, product):
    stmt = insert(Product).values(
        id=product.id,
        title=product.title,
        price=product.price,
        store_id=product.store_id
    ).on_conflict_do_update(
        index_elements=[Product.id],
        set_={"title": product.title, "price": product.price, "store_id": product.store_id}
    )
    try:
        db.execute(stmt)
        db.commit()
        logger.info(f"Producto {product.id} insertado o actualizado.")
    except IntegrityError:
        db.rollback()
        logger.error(f"Error al insertar/actualizar producto {product.id}.")


def delete_missing_products(db: Session, existing_ids):
    deleted = db.query(Product).filter(Product.id.not_in(existing_ids)).delete(synchronize_session=False)
    db.commit()
    logger.info(f"{deleted} productos eliminados que no estaban en el portal CSV.")


def get_all_products(db: Session):
    products = db.query(Product).all()
    logger.info(f"Se obtuvieron {len(products)} productos de la base de datos.")
    return products
