def process_numbers(x, y):
    if x == y:
        print("Числа не повинні бути рівні одне одному.")
    else:
        if x < y:
            x = (x + y) / 2
            y = 2 * x * y
        else:
            y = (x + y) / 2
            x = 2 * x * y

        print(f"Нове значення x: {x}")
        print(f"Нове значення y: {y}")

x = float(input("Введіть перше число (x): "))
y = float(input("Введіть друге число (y): "))

process_numbers(x, y)

