# Первый вариант решения
number: int = int(input("Введите целое число: "))

if number > 0:
    print(1)
elif number < 0:
    print(-1)
else:
    print(0)

# Второй вариант решения

result: int = 1 if number > 0 else (-1 if number < 0 else 0)
print(result)
