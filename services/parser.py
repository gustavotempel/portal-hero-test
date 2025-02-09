from utils.file_reader import read_csv
from utils.validators import validate_product
from models.product import Product
from core.logger import logger

def process_csv(file_path):
    rows = read_csv(file_path)
    products = []
    for row in rows:
        validated_product = validate_product(row)
        if validated_product:
            products.append(Product(**validated_product))
    logger.info(f"Procesados {len(products)} productos del archivo CSV.")
    return products
