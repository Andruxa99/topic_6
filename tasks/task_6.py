year: int = int(input("Введите год: "))  # Пользовательский ввод
month: int = int(input("Введите месяц: "))

if year % 4 != 0:
    print("нет")
elif year % 100 != 0:
    print("нет")
elif year % 400 == 0:
    print("да")
else:
    print("нет")

