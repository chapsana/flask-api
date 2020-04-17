import pytest

from app import app,db


@pytest.fixture(name="app")
def fixture_app():
    db.create_all()
    app.testing = True
    yield app
    app.testing = False


@pytest.fixture
def client(app):
    return app.test_client()
