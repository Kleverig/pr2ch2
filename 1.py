def process_numbers(a, b, c):
    result = []
    for num in [a, b, c]:
        if num >= 0:
            result.append(num ** 2)
        else:
            result.append(num ** 4)
    return result

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

processed_numbers = process_numbers(a, b, c)

print("Оброблені числа:", processed_numbers)
