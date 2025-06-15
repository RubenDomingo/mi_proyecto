import pytest

from mi_proyecto.romanos import ( num_romanos )
def test_get_romano_valid():
    test = num_romanos(1)
    assert test == 'I'

def test_get_romano_invalid():
    test = num_romanos(1)
    assert test == 0