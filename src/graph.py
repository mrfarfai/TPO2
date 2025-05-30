import csv
import matplotlib.pyplot as plt

def plot_from_csv(filename, delimiter=','):
    x_vals_neg = []
    y_vals_neg = []
    x_vals = []
    y_vals = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        header = next(reader)  # пропускаем заголовок

        for row in reader:
            data = row[0].split(';')
            try:
                x = float(data[0])
                y = float(data[1])
            except ValueError:
                continue


            if round(x, 2) < 0:
                x_vals_neg.append(x)
                y_vals_neg.append(y)
            elif round(x, 2) > 0:
                x_vals.append(x)
                y_vals.append(y)

    plt.figure(figsize=(8,5))
    plt.plot(x_vals_neg, y_vals_neg, marker='o', linestyle='-', label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции из CSV')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции из CSV')
    plt.grid(True)
    plt.legend()
    plt.show()

plot_from_csv('output.csv')
