import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.app import app
from app.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)
    # gerenciamento de contexto (with) para criar
    # e destruir a sessão do banco de dados
    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
