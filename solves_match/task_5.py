number = int(input("Введите целое число: "))

match number:
    case _ if number % 2 == 0:
        print("Число", number, "является четным")
    case _ if number * 3 > 20:
        print("Результат умножения", number, "на 3 больше 20")
    case _:
        print("Число", number, "не соответствует условиям")
