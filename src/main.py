import csv
from dotenv import load_dotenv
import os

load_dotenv()

USE_STUBS = os.getenv("USE_STUBS", "false").lower() == "true"

if USE_STUBS:
    from stubs import sin, cos, sec, cot, ln, log_3, log_5, log_10
else:
    from functions import sin, cos, sec, cot, ln, log_3, log_5, log_10

def system_function(x):
    x_rounded = round(x, 2)
    if x_rounded < 0:
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



def write_results_to_csv(filename, start, end, step, delimiter=','):
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)

        x = start
        while x <= end:
            try:
                y = system_function(x)
            except Exception as e:
                y = str(e)
            writer.writerow([x, y])
            x += step

write_results_to_csv('output.csv', -2.0, 2.0, 0.1, delimiter=';')