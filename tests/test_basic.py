import math_lib as ml

def test_sq():
    assert ml.sq(16) == 4

def test_ex():
    assert round(ml.ex(1),3) == 2.718

def test_lg():
    assert ml.lg(1001, 10) ==2

def test_fct():
    assert ml.fct(5) == 120