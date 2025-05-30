import pytest
import math
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from functions import sin, cos, sec, cot, ln, log_3, log_5, log_10

def test_sin_cos():
    assert math.isclose(sin(0), 0, abs_tol=1e-9)
    assert math.isclose(cos(0), 1, abs_tol=1e-9)

def test_sec_valid():
    assert math.isclose(sec(0), 1, abs_tol=1e-9)
    with pytest.raises(ValueError):
        sec(math.pi / 2)  # cos(pi/2) ≈ 0, sec не определён

def test_cot_valid():
    assert math.isclose(cot(math.pi / 4), 1, abs_tol=1e-9)
    with pytest.raises(ValueError):
        cot(0)  # tan(0) = 0, cot не определён

def test_ln_valid():
    assert math.isclose(ln(math.e), 1, abs_tol=1e-9)
    with pytest.raises(ValueError):
        ln(0)
    with pytest.raises(ValueError):
        ln(-1)

def test_log_3_5_10():
    assert math.isclose(log_3(3), 1, abs_tol=1e-9)
    assert math.isclose(log_5(5), 1, abs_tol=1e-9)
    assert math.isclose(log_10(10), 1, abs_tol=1e-9)
    with pytest.raises(ValueError):
        log_3(0)
    with pytest.raises(ValueError):
        log_5(-5)
