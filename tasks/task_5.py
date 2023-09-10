number: int = int(input("Введите целое число: "))  # пользовательский ввод

if number % 2 == 0:
    print("Число", number, "является четным")
elif number * 3 > 20:
    print("Результат умножения", number, "на 3 больше 20")
else:
    print("Число", number, "не соответствует условиям")
