import pytest

# Define a fixture for setup and teardown
@pytest.fixture
def setup():
    print("Started")
    yield
    print("End.")

# Test function using the fixture
def test_mul_of_2(setup):
    assert 2 * 2 == 4

# Parameterized test function using the fixture
@pytest.mark.parametrize("input, expected", [
    (1, 2),
    (2, 4),
    (3, 6)
])
def test_multiplication(setup, input, expected):
    assert input * 2 == expected
