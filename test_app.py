import pytest
from application import calculate_balance

def test_calculate_balance():
    assert calculate_balance(100, 50) == 150
    assert calculate_balance(100, -50) == 50
    assert calculate_balance(100, 0) == 100
    assert calculate_balance(0, 100) == 100

if __name__ == '__main__':
    pytest.main()
