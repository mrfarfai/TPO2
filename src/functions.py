import math

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def sec(x):
    c = cos(x)
    if abs(c) < 1e-12:
        raise ValueError("sec(x) не определён при cos(x) близком к 0")
    return 1 / c

def cot(x):
    t = math.tan(x)
    if abs(t) < 1e-12:
        raise ValueError("cot(x) не определён при tan(x) близком к 0")
    return 1 / t

def ln(x):
    if x <= 0:
        raise ValueError("ln(x) определён только для x > 0")
    return math.log(x)

def log_base(x, base):
    if x <= 0:
        raise ValueError(f"логарифм по основанию {base} определён только для x > 0")
    return math.log(x, base)

def log_3(x):
    return log_base(x, 3)

def log_5(x):
    return log_base(x, 5)

def log_10(x):
    return log_base(x, 10)
