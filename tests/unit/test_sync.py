import csv, pytest, tempfile
from app.models.product import Product
from app.services.sync import sync_products

@pytest.fixture
def sample_csv():
    """Crea un archivo CSV temporal para pruebas"""
    data = [
        ["product_id", "title", "price", "store_id"],
        [1, "Producto A", 10.99, 1],
        [2, "Producto B", 5.99, 2]
    ]
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, newline="") as temp_csv:
        writer = csv.writer(temp_csv)
        writer.writerows(data)
        return temp_csv.name

def test_sync_insert_new_products(db_session, sample_csv):
    """Prueba la inserción de nuevos productos desde el CSV"""
    sync_products(db_session, sample_csv)

    products = db_session.query(Product).all()
    assert len(products) == 2
    assert products[0].title == "Producto A"
    assert products[1].title == "Producto B"
