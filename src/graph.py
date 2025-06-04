import csv
import matplotlib.pyplot as plt

def plot_from_csv(filename, delimiter=','):
    x_vals = []
    y_vals = []
    x_vals_neg = []
    y_vals_neg = []
    x_vals_pos = []
    y_vals_pos = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        next(reader)

        for row in reader:
            try:
                x = float(row[0])
                y = float(row[1])

                x_vals.append(x)
                y_vals.append(y)

                if x < 0:
                    x_vals_neg.append(x)
                    y_vals_neg.append(y)
                elif x > 0:
                    x_vals_pos.append(x)
                    y_vals_pos.append(y)
            except ValueError:
                continue

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', label='f(x) (все данные)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции из CSV (все данные)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals_neg, y_vals_neg, marker='o', linestyle='-', color='r', label='f(x) (x < 0)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции для x < 0')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals_pos, y_vals_pos, marker='o', linestyle='-', color='g', label='f(x) (x > 0)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции для x > 0')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_from_csv('test_module.csv', delimiter=';')
