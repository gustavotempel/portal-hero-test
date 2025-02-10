import csv, pytest, tempfile

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base


TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Crea una base de datos en memoria para cada prueba"""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def sample_csv():
    """Crea un archivo CSV temporal para pruebas"""
    data = [
        ["product_id", "title", "price", "store_id"],
        [1, "Producto A", 10.99, 1],
        [2, "Producto B", 5.99, 2]
    ]
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as temp_csv:
        temp_csv.write("\n".join([",".join(map(str, row)) for row in data]))
        temp_csv.flush()
        temp_csv.close() 
        yield temp_csv.name

    import os
    os.remove(temp_csv.name)
