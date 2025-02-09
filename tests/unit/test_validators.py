from utils.validators import validate_product

def test_validate_product():
    row = {"product_id": "1", "title": "Producto A", "price": "9.99", "store_id": "2"}
    result = validate_product(row)
    assert result["id"] == 1
    assert result["title"] == "Producto A"
    assert result["price"] == 9.99
    assert result["store_id"] == 2

def test_validate_product_error():
    row = {"product_id": "2", "title": "Producto B", "price": "9,99", "store_id": "3"}
    result = validate_product(row)
    assert result is None
