from app.core.logger import logger
from app.models.product import Product
from app.utils.file_reader import read_csv
from app.utils.validators import validate_product


def process_csv(file_path):
    rows = read_csv(file_path)
    products = []
    for row in rows:
        validated_product = validate_product(row)
        if validated_product:
            products.append(Product(**validated_product))
    logger.info(f"Procesados {len(products)} productos del archivo CSV.")
    return products
