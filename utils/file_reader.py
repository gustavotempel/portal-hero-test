import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def read_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            logger.info(f"Archivo CSV '{file_path}' leído correctamente.")
            return list(reader)
    except FileNotFoundError:
        logger.error(f"Error: Archivo '{file_path}' no encontrado.")
    except csv.Error:
        logger.error(f"Error: Problema al parsear el archivo CSV '{file_path}'.")
    return []
