import pytest

from mi_proyecto.binario import ( get_binario )

def test_get_binario_valid():
    test = get_binario(5)
    assert test == '101'

def test_get_binario_invalid():
    test = get_binario(5)
    assert test == '1'