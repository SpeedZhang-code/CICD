import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    # 測試是否會正確拋出除以零的錯誤
    with pytest.raises(ValueError):
        divide(10, 0)
