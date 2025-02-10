import pytest
import os
from app.services.parser import process_csv

TEST_CSV_FILE = "test_process.csv"

@pytest.fixture
def create_test_csv():
    with open(TEST_CSV_FILE, "w", encoding="utf-8") as f:
        f.write("product_id,title,price,store_id\n")
        f.write("1,Producto A,9.99,2\n")
        f.write("2,Producto B,19.99,3\n")
        f.write("X,Producto C,invalid_price,4\n")
    yield
    os.remove(TEST_CSV_FILE)

def test_process_csv(create_test_csv):
    data = process_csv(TEST_CSV_FILE)
    assert len(data) == 2
    assert data[0].id == 1
    assert data[0].title == "Producto A"
    assert data[0].price == 9.99
    assert data[0].store_id == 2
    assert data[1].id == 2
    assert data[1].title == "Producto B"
    assert data[1].store_id == 3
    assert data[1].price == 19.99

def test_process_csv_file_not_found():
    data = process_csv("non_existent.csv")
    assert data == []
