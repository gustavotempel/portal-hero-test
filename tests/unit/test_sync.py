from app.models.product import Product
from app.services.sync import sync_products


def test_sync_insert_new_products(db_session, sample_csv):
    """Prueba la inserción de nuevos productos desde el CSV"""
    with open(sample_csv, "rb") as file:
        sync_products(db_session, file.name)
        products = db_session.query(Product).all()

    assert len(products) == 2
    assert products[0].title == "Producto A"
    assert products[1].title == "Producto B"
