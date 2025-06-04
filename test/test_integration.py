import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from main import system_function


@pytest.fixture
def mock_functions(mocker):
    mock_sin = mocker.patch('main.sin', return_value=1)
    mock_cos = mocker.patch('main.cos', return_value=1)
    mock_sec = mocker.patch('main.sec', return_value=1)
    mock_cot = mocker.patch('main.cot', return_value=1)
    mock_ln = mocker.patch('main.ln', return_value=1)
    mock_log_3 = mocker.patch('main.log_3', return_value=1)
    mock_log_5 = mocker.patch('main.log_5', return_value=1)
    mock_log_10 = mocker.patch('main.log_10', return_value=1)

    return {
        'sin': mock_sin,
        'cos': mock_cos,
        'sec': mock_sec,
        'cot': mock_cot,
        'ln': mock_ln,
        'log_3': mock_log_3,
        'log_5': mock_log_5,
        'log_10': mock_log_10
    }


def test_system_function_stub_negative(mock_functions):
    mock_functions['sin'].return_value = 1
    mock_functions['cos'].return_value = 1
    mock_functions['sec'].return_value = 1
    mock_functions['cot'].return_value = 1

    result = system_function(-1)
    assert isinstance(result, float)


def test_system_function_stub_positive(mock_functions):
    mock_functions['log_5'].return_value = 1
    mock_functions['ln'].return_value = 1
    mock_functions['log_3'].return_value = 1
    mock_functions['log_10'].return_value = 1

    result = system_function(1)
    assert isinstance(result, float)


def test_system_function_zero(mock_functions):
    mock_functions['sin'].return_value = 0
    mock_functions['cos'].return_value = 1
    mock_functions['sec'].return_value = 1
    mock_functions['cot'].return_value = 1

    with pytest.raises(ValueError):
        system_function(0)


def test_system_function_log_error(mock_functions):
    mock_functions['log_5'].return_value = 0

    with pytest.raises(ValueError):
        system_function(1)
