number: int = int(input("Введите целое число: "))

match number:
    case _ if number > 0:
        print(1)
    case _ if number < 0:
        print(-1)
    case _:
        print(0)
        