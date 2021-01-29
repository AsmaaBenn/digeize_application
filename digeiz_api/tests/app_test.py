"""
This is a /tests/app_test.py file.

Series of tests for different end points.
"""
import pytest
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy


from app import app
db = SQLAlchemy(app)

TEST_DB = "data_app.db"

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    app.config["DATABASE"] = BASE_DIR.joinpath(TEST_DB)

    db.create_all()  # setup
    yield app.test_client()  # tests run here
    db.drop_all()  # teardown


def test_index(client):
    """Test that messages work."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Welcome to this fantastic app!"


def test_database(client):
    """Initial test. ensure that the database exists."""
    tester = Path("data_app.db").is_file()
    assert tester
"""
************************************************************************
******************** Test the Account end points ***********************
************************************************************************
"""

def test_get_accounts(client):
    """Ensure that gets malls list work."""
    response = client.get("/accounts")
    assert response.status_code == 200


def test_post_account(client):
    """Ensure that user can post messages."""
    response = client.post("/account", data=dict(
        name="asmaa"), follow_redirects=True)
    assert response.status_code == 201


def test_delete_account(client):
    """Test API can delete an existing account. (DELETE request)."""
    response = client.delete('/account/asmaa')
    assert response.status_code == 200

"""
************************************************************************
******************** Test the Mall end point ***************************
************************************************************************
"""

def test_get_malls(client):
    """Ensure that gets malls list work."""
    response = client.get("/malls")
    assert response.status_code == 200


def test_post_mall(client):
    """Ensure that user can post a mall."""
    response = client.post("/mall/le chesney", data=dict(
        address="le chesney", account_id=1), follow_redirects=True)
    assert response.status_code == 201


def test_delete_mall(client):
    """Test API can delete an existing mall. (DELETE request)."""
    response = client.delete('/mall/le chesney')
    assert response.status_code == 200

"""
************************************************************************
******************** Test the Unit end point ***************************
************************************************************************
"""

def test_get_units(client):
    """Ensure that gets units list work."""
    response = client.get("/units")
    assert response.status_code == 200


def test_post_unit(client):
    """Ensure that user can post unit."""
    response = client.post("/unit", data=dict(
        name="mango", mall_id=1), follow_redirects=True)
    assert response.status_code == 201


def test_delete_unit(client):
    """Test API can delete an existing unit. (DELETE request)."""
    response = client.delete("/unit/3")
    assert response.status_code == 200
