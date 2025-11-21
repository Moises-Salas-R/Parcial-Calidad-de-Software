import pytest

from src.Calculadora import Dividir, Multiplicar, Restar, Sumar


def test_Sumar():
    assert Sumar(3, 5) == 8
    assert Sumar(-2, 2) == 0
    assert Sumar(0, 0) == 0
    assert Sumar(7, -2) == 5
    assert Sumar(-1, -10) == -11

def test_Restar():
    assert Restar(10, 5) == 5
    assert Restar(0, 0) == 0
    assert Restar(-3, -2) == -1
    assert Restar(-15, 2) == -17
    assert Restar(-20, -20) == 0

def test_Multiplicar():
    assert Multiplicar(4, 5) == 20
    assert Multiplicar(-2, 3) == -6
    assert Multiplicar(0, 10) == 0
    assert Multiplicar(0, 0) == 0
    assert Multiplicar(-2, -2) == 4

def test_Dividir():
    assert Dividir(10, 2) == 5
    assert Dividir(-6, -2) == 3
    assert Dividir(-8, -4) == 2

def test_Dividir_por_cero():
    with pytest.raises(ValueError):
        Dividir(5, 0)
