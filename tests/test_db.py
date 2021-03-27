import json
import pytest
from tinydb import TinyDB

@pytest.fixture
def db():
    db = TinyDB("db.json")
    print("\n Setup DB")
    yield db
    db.truncate()
    print("\n Teardown DB")

def test_insert_one(db):
    db.insert({"name": "Bob"})
    assert len(db.all()) == 1
    print("Test finished")

def test_insert_multiple(db):
    db.insert_multiple(
        [{"name": "Alice"}, {"name": "Carlos"}]
    )
    assert len(db.all()) == 2