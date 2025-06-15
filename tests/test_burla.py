import pytest

from mi_proyecto.burla import ( burla_A, burla_E, burla_I, burla_O, burla_U )

def test_burla_A_valid():
    test = burla_A('No me gustan los macarrones')
    assert test == 'Na ma gastan las macarranas'

def test_burla_A_invalid():
    test = burla_A('No me gustan los macarrones')
    assert test == 'Ne me gesten les mecerrenes'

def test_burla_E_valid():
    test = burla_E('No me gustan los macarrones')
    assert test == 'Ne me gesten les mecerrenes'

def test_burla_E_invalid():
    test = burla_E('No me gustan los macarrones')
    assert test == 'Na ma gastan las macarranas'

def test_burla_I_valid():
    test = burla_I('No me gustan los macarrones')
    assert test == 'Ni mi gistin lis micirrinis'

def test_burla_I_invalid():
    test = burla_I('No me gustan los macarrones')
    assert test == 'Na ma gastan las macarranas'

def test_burla_O_valid():
    test = burla_O('No me gustan los macarrones')
    assert test == 'No mo goston los mocorronos'

def test_burla_O_invalid():
    test = burla_O('No me gustan los macarrones')
    assert test == 'Na ma gastan las macarranas'

def test_burla_U_valid():
    test = burla_U('No me gustan los macarrones')
    assert test == 'Nu mu gustun lus mucurrunus'

def test_burla_U_invalid():
    test = burla_U('No me gustan los macarrones')
    assert test == 'Na ma gastan las macarranas'