# Первый вариант решения

number: int = int(input("Введите целое число: "))  # пользовательский ввод
if number == 1:
    print("число положительное")
elif number == -1:
    print("число отрицательное")
else:
    number = 0
    print("0")

# Второй вариант решения

# result = "Положительное число" if number > 0 \
#     else "Отрицательное число или ноль"
# print(result)
