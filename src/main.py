import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from functions import sin, cos, sec, cot, ln, log_3, log_5, log_10
from decimal import Decimal, getcontext

getcontext().prec = 6

def system_function(x):
    x_rounded = Decimal(x).quantize(Decimal('0.0001'))

    if x_rounded == 0:
        raise ValueError("Ошибка: x = 0 приводит к делению на ноль")

    if x_rounded < 0:
        numerator = (sin(x) - cos(x)) + sin(x) + cos(x)
        denominator = sec(x)
        trig_part = numerator / denominator
        result = trig_part * (sec(x) - cot(x))
        return result
    else:
        denom = log_5(x)
        if abs(denom) < 1e-12:
            raise ValueError(f"Ошибка: log_5({x}) приводит к делению на ноль")

        part1 = (ln(x) / denom) * (log_3(x) ** 3)
        part2 = (ln(x) + denom) - (log_10(x) ** 3)
        part3 = log_3(x) / log_10(x)
        return (part1 + part2) * part3
