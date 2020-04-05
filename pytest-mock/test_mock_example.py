import pytest
from mock import Mock
from mock_example import DB, Person

@pytest.fixture
def mock_db():
    return Mock(spec=DB)

def test_save_persistent_to_db(mock_db):
    mat = Person("Mattia", mock_db)
    mat.save()
    mock_db.persist.assert_called_with(mat) # assert the method has been called with the param self=mat
    # Passes

def test_fail_not_called(mock_db):
    mat = Person("Mattia", mock_db)
    lui = Person("Luigi", mock_db)
    mat.save()
    mock_db.persist.assert_called_with(lui)
    # Fails

def test_any_call(mock_db):
    mock_db.persist(1)
    mock_db.persist(2)
    mock_db.persist.assert_any_call(1)
    # Passes

def test_any_call_failure(mock_db):
    mock_db.persist(1)
    mock_db.persist(2)
    mock_db.persist.assert_any_call(3)
    # Fails
