def determine_point_location(x, y):
    if x == 0 and y == 0:
        return "Точка A знаходиться в початку координат."
    elif x == 0:
        return "Точка A знаходиться на осі Y."
    elif y == 0:
        return "Точка A знаходиться на осі X."
    elif x > 0 and y > 0:
        return "Точка A знаходиться в першому квадранті."
    elif x < 0 and y > 0:
        return "Точка A знаходиться в другому квадранті."
    elif x < 0 and y < 0:
        return "Точка A знаходиться в третьому квадранті."
    elif x > 0 and y < 0:
        return "Точка A знаходиться в четвертому квадранті."

x = float(input("Введіть координату x точки A: "))
y = float(input("Введіть координату y точки A: "))

result = determine_point_location(x, y)
print(result)

