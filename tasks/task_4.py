number_1: int = int(input("Введите первое число: "))
number_2: int = int(input("Введите второе число: "))
number_3: int = int(input("Введите третье число: "))

if number_1 == number_2 == number_3:
    print("Все числа равны")
elif number_1 > number_2 and number_1 > number_3:
    print("Наибольшее число:", number_1)
elif number_2 > number_3:
    print("Наибольшее число:", number_2)
else:
    print("Наибольшее число:", number_3)
