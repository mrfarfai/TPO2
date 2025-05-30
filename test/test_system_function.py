import sys
import os
import pytest
from dotenv import load_dotenv

load_dotenv()
USE_STUBS = os.getenv("USE_STUBS", "false").lower() == "true"

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from main import system_function

def test_system_function_negative():
    result = system_function(-1)
    assert isinstance(result, float)

@pytest.mark.skipif(USE_STUBS, reason="Пропускаем тесты с ошибками при использовании заглушек")
def test_system_function_zero():
    with pytest.raises(ValueError):
        system_function(0)

@pytest.mark.skipif(USE_STUBS, reason="Пропускаем тесты с ошибками при использовании заглушек")
def test_system_function_positive():
    with pytest.raises(ValueError):
        system_function(1)

def test_system_function_positive_valid():
    result = system_function(1.1)
    assert isinstance(result, float)
