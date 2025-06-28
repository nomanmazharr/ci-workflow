import pytest
def square(n):
    return n **2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

def test_square():
    assert square(2) == 4, "Test Failed, Square of 2 is 4"
    assert square(5) == 25, "Test Failed, Square of 5 is 25"

def test_cube():
    assert cube(2) == 8, "Test Failed, Cube of 2 is 8"
    assert cube(5) == 125, "Test Failed, Cube of 5 is 125"

def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed, fifth_power of 2 is 8"
    assert fifth_power(5) == 3125, "Test Failed, fifth_power of 5 is 3125"

def test_input():
    with pytest.raises(TypeError):
        square('string')
