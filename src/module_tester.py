import csv
import sys
import os
from decimal import Decimal, getcontext

getcontext().prec = 6

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from functions import sin, cos, sec, cot, ln, log_3, log_5, log_10
from main import system_function

FUNCTIONS = {
    'sin': sin,
    'cos': cos,
    'sec': sec,
    'cot': cot,
    'ln': ln,
    'log_3': log_3,
    'log_5': log_5,
    'log_10': log_10,
    'system_function': system_function,
}

def input_with_back(prompt):
    val = input(prompt).strip()
    if val.lower() == 'back':
        return None
    return val

def select_function():
    while True:
        print("\nДоступные функции для тестирования:")
        for f in FUNCTIONS:
            print(f"- {f}")

        func_name = input_with_back("Введите имя функции для тестирования (или 'back' для выхода): ")
        if func_name is None:
            return None
        if func_name not in FUNCTIONS:
            print("Функция не найдена! Попробуйте снова.")
            continue
        return func_name

def input_float(prompt, min_val = None):
    while True:
        val = input_with_back(prompt)
        if val is None:
            return None
        try:
            value = float(val)
            if min_val is not None:
                if value < min_val:
                    print("Ошибка: значение должно быть больше или равен " + str(min_val))
                    continue
            return Decimal(value)
        except ValueError:
            print("Ошибка: введите корректное числовое значение.")

def get_interval_params():
    while True:
        start = input_float("Введите начальное значение X (или 'back' для возврата): ")
        if start is None:
            return None

        end = input_float("Введите конечное значение X (или 'back' для возврата): ")
        if end is None:
            continue

        step = input_float("Введите шаг изменения X (положительное число) (или 'back' для возврата): ", 0.0001)
        if step is None:
            continue

        return start, end, step

def main():
    print("=== Тестирование функций с записью результатов в CSV ===")
    while True:
        func_name = select_function()
        if func_name is None:
            print("Выход из программы.")
            break

        interval = get_interval_params()
        if interval is None:
            continue

        start, end, step = interval

        delimiter = input("Введите разделитель для CSV (например, , или ;), Enter для запятой: ").strip()
        if not delimiter:
            delimiter = ','

        func = FUNCTIONS[func_name]
        filename = "test_module.csv"

        with open(filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=delimiter)
            writer.writerow(['X', f'Результат {func_name}(X)'])

            count = int((end - start) / step) + 1
            for i in range(count):
                x = start + i * step
                try:
                    x_rounded = x.quantize(Decimal('0.0001'))
                    y = func(x_rounded)
                except Exception as e:
                    y = f"Ошибка: {str(e)}"
                writer.writerow([round(x_rounded, 4), y])

        print(f"\nРезультаты функции '{func_name}' записаны в файл '{filename}'.\n")

if __name__ == "__main__":
    main()
