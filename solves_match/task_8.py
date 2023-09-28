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

match magic:
    case "Призыв":
        print("Сумма магических сил чисел:", number_1 + number_2)
    case "Трансформация":
        print("Трансформированное число:", number_1 - number_2)
    case "Объединение":
        print("Произведение магических чисел:", number_1 * number_2)
    case "Исчезновение":
        match number_2:
            case 0:
                print("Ошибка: Второе число равно нулю!")
            case _:
                print("Исчезновение", number_1 / number_2)
    case _:
        print("Ошибка: Некорректная операция")
