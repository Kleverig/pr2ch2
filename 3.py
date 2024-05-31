def check_triangle(angle1, angle2):
    if angle1 + angle2 < 180:
        return "Так, такий трикутник існує."
    else:
        return "Ні, такий трикутник не існує."

def check_right_triangle(angle1, angle2):
    if angle1 == 90 or angle2 == 90 or angle1 + angle2 == 90:
        return "Трикутник є прямокутним."
    else:
        return "Трикутник не є прямокутним."

angle1 = float(input("Введіть перший кут трикутника в градусах: "))
angle2 = float(input("Введіть другий кут трикутника в градусах: "))

triangle_existence = check_triangle(angle1, angle2)
print(triangle_existence)

if triangle_existence == "Так, такий трикутник існує.":
    right_triangle_check = check_right_triangle(angle1, angle2)
    print(right_triangle_check)
