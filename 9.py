def count_integers(a, b, c):
    count = 0
    if a.is_integer():
        count += 1
    if b.is_integer():
        count += 1
    if c.is_integer():
        count += 1
    return count

a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))

integer_count = count_integers(a, b, c)

print(f"Кількість цілих чисел: {integer_count}")
