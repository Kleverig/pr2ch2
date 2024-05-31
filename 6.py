def process_numbers(a, b):
    if a != b:
        max_value = max(a, b)
        a = max_value
        b = max_value
    else:
        a = 0
        b = 0
    return a, b

a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

a, b = process_numbers(a, b)

print(f"Нові значення: a = {a}, b = {b}")
