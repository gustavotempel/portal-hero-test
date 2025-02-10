from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.product import Product


def insert_or_update_product(db: Session, product):
    existing_product = db.query(Product).filter(Product.id == product.id).first()
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
        if existing_product:
            logger.info(f"Producto {product.id} actualizado.")
        else:
            logger.info(f"Producto {product.id} insertado.")
    except IntegrityError:
        db.rollback()
        logger.error(f"Error al insertar/actualizar producto {product.id}.")


def delete_missing_products(db: Session, existing_ids):
    all_products = db.query(Product).all()
    products_to_delete = [p.id for p in all_products if p.id not in existing_ids]
    if products_to_delete:
        db.query(Product).filter(Product.id.in_(products_to_delete)).delete(synchronize_session=False)
        db.commit()
        for product_id in products_to_delete:
            logger.info(f"Producto {product_id} eliminado.")


def get_all_products(db: Session):
    products = db.query(Product).all()
    logger.info(f"Se obtuvieron {len(products)} productos de la base de datos.")
    return products
