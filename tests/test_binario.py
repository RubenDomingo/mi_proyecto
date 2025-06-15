import pytest

from mi_proyecto.binario import ( get_binario )

def test_get_binario_valid():
    assert get_binario(5) == '101'
    assert get_binario(10) == '1010'
    assert get_binario(15) == '1111'

def test_get_binario_invalid():
    assert get_binario(0) == '1'
    assert get_binario('1')
    assert get_binario(3.14)