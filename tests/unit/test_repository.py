from app.models.product import Product
from app.services.repository import insert_or_update_product, get_all_products


def test_insert_or_update_product(db_session):
    """Prueba la inserción y actualización de productos"""
    product_data = Product(id=1, title="Test Product", price=10.99, store_id=1)
    insert_or_update_product(db_session, product_data)

    products = get_all_products(db_session)
    assert len(products) == 1
    assert products[0].title == "Test Product"
    assert products[0].price == 10.99
    assert products[0].store_id == 1

    updated_product = Product(id=1, title="Updated Product", price=15.99, store_id=1)
    insert_or_update_product(db_session, updated_product)

    products = get_all_products(db_session)
    assert len(products) == 1
    assert products[0].title == "Updated Product"
    assert products[0].price == 15.99
    assert products[0].store_id == 1

def test_get_all_products_empty(db_session):
    """Verifica que se retorna una lista vacía si no hay productos"""
    products = get_all_products(db_session)
    assert len(products) == 0
