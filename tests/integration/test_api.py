import pytest

from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="module")
def client():
    """Cliente de pruebas para la API"""
    return TestClient(app)

def test_create_product(client, db_session, sample_csv):
    """Prueba la creación de un producto vía API"""
    with open(sample_csv, "rb") as file:
        files = {"file": ("test.csv", file, "text/csv")}
        response = client.post("/products/", files=files)
    assert response.status_code == 200
    assert response.json() == {"message": "Productos insertados o actualizados."}

def test_get_products(client, db_session):
    """Prueba la obtención de todos los productos vía API"""
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
