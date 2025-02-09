import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.database import Base, get_db
from models.product import Product
from services.repository import insert_or_update_product, get_all_products

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Crea una nueva sesión de base de datos para cada prueba"""
    Base.metadata.create_all(bind=engine) 
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_insert_or_update_product(db_session):
    """Prueba la inserción y actualización de productos"""
    product_data = Product(id=1, title="Test Product", price=10.99, store_id=1)
    insert_or_update_product(db_session, product_data)

    products = get_all_products(db_session)
    assert len(products) == 1
    assert products[0].title == "Test Product"


    updated_product = Product(id=1, title="Updated Product", price=15.99, store_id=1)
    insert_or_update_product(db_session, updated_product)

    products = get_all_products(db_session)
    assert len(products) == 1
    assert products[0].title == "Updated Product"
    assert products[0].price == 15.99

def test_get_all_products_empty(db_session):
    """Verifica que se retorna una lista vacía si no hay productos"""
    products = get_all_products(db_session)
    assert len(products) == 0
