from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    store_id = Column(Integer)

    def __repr__(self):
        return f"<Product {self.id} - {self.title} - {self.price} - {self.store_id}>"
