from app.models.product import Product

def test_product_model():
    product = Product(id=1, title='Test Product', price=10.0, store_id=1)
    assert product.id == 1
    assert product.title == 'Test Product'
    assert product.price == 10.0
    assert product.store_id == 1
    assert str(product) == '<Product 1 - Test Product - 10.0 - 1>'