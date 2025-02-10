from app.core.logger import logger


def validate_product(row):
    try:
        return {
            "id": int(row['product_id']),
            "title": str(row['title']),
            "price": float(row['price']),
            "store_id": int(row['store_id'])
        }
    except ValueError:
        logger.warning(f"Error de conversión en la fila: {row}")
        return None
