def check_divisor(a, b, c, k):
    if a % k == 0:
        print(f"{k} є дільником числа {a}.")
    else:
        print(f"{k} не є дільником числа {a}.")

    if b % k == 0:
        print(f"{k} є дільником числа {b}.")
    else:
        print(f"{k} не є дільником числа {b}.")

    if c % k == 0:
        print(f"{k} є дільником числа {c}.")
    else:
        print(f"{k} не є дільником числа {c}.")

a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))
c = int(input("Введіть третє число (c): "))
k = int(input("Введіть число-дільник (k): "))

check_divisor(a, b, c, k)
