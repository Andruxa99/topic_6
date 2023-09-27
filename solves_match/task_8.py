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

match number_1, number_2, magic:
    case _ if magic == "Призыв":
        print("Сумма магических сил чисел:", number_1 + number_2)
    case _ if magic == "Трансформация":
        print("Трансформированное число:", number_1 - number_2)
    case _ if magic == "Объединение":
        print("Произведение магических чисел:", number_1 * number_2)
    case _ if number_2 == 0:
        print("Ошибка: Второе число равно нулю!")
    case _ if magic == "Исчезновение":
        print("Исчезновение", number_1 / number_2)
    case _:
        print("Ошибка: Некорректная операция")

