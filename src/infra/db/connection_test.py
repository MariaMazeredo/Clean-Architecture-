import pytest
from src.infra.db.settings.connection import DBConnectionHandler

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handle = DBConnectionHandler()
    enginer=db_connection_handle.get_engine()

    assert enginer is not None

   