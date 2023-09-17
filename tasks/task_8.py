print("Доступные операции: "
      "Призыв",
      "Трансформация",
      "Объединение",
      "Исчезновение",
      sep=", "
      )

number_1: float = float(input("Введите первое число: "))
number_2: float = float(input("Введите второе число: "))
magic: str = input("Введите магическую операцию: ")

if magic == "Призыв":
    print("Сумма магических сил чисел:", number_1 + number_2)
elif magic == "Трансформация":
    print("Трансформированное число:", number_1 - number_2)
elif magic == "Объединение":
    print("Произведение магических чисел:", number_1 * number_2)
elif magic == "Исчезновение":
    if number_2 == 0:
        print("Ошибка: Второе число равно нулю!")
    else:
        print("Исчезновение", number_1 / number_2)
else:
    print("Ошибка: Некорректная операция")
