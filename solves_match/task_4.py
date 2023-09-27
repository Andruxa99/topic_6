number_1: int = int(input("Введите первое число: "))
number_2: int = int(input("Введите второе число: "))
number_3: int = int(input("Введите третье число: "))

match number_1, number_2, number_3:
    case _ if number_1 == number_2 == number_3:
        print("Все числа равны")
    case _ if number_1 > number_2 and number_1 > number_3:
        print("Наибольшее число:", number_1)
    case _ if number_2 > number_3:
        print("Наибольшее число:", number_2)
    case _:
        print("Наибольшее число:", number_3)
