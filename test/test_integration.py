import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from stubs import sin, cos, sec, cot, ln, log_3, log_5, log_10

def system_function_stub(x):
    if round(x, 2) < 0:
        numerator = (sin(x) - cos(x)) + sin(x) + cos(x)
        denominator = sec(x)
        trig_part = numerator / denominator
        result = trig_part * (sec(x) - cot(x))
        return result
    else:
        denom = log_5(x)
        if abs(denom) < 1e-12:
            raise ValueError("Деление на ноль в log_5(x)")
        part1 = (ln(x) / denom) * (log_3(x) ** 3)
        part2 = (ln(x) + denom) - (log_10(x) ** 3)
        part3 = log_3(x) / log_10(x)
        return (part1 + part2) * part3

def test_system_function_stub_negative():
    assert system_function_stub(-1) == 0.5

def test_system_function_stub_positive():
    assert system_function_stub(1) == 2.0

def test_system_function_stub_zero():
    result = system_function_stub(0)
    assert isinstance(result, float)
