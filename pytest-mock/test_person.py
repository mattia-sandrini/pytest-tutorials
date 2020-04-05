import pytest
from person import Person


@pytest.fixture
def person():
    return Person()


def test_greet(person):
    greeting = person.greet()
    assert greeting == "hi there!"
