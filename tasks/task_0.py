color: str = input("Введите ваш любимый цвет: ")  # ввод пользователя

if color == "солнечно-желтый":
    print("Это цвет радости и счастья!")
elif color == "небесно-голубой":
    print("Это цвет радости и счастья!")
else:
    print("Это тоже хороший цвет!")

# -------------------------- №1
if color == "солнечно-желтый" or color == "небесно-голубой":
    print("Это цвет радости и счастья!")
else:
    print("Это тоже хороший цвет!")

# -------------------------- №2
if color in ("солнечно-желтый", "небесно-голубой"):
    print("Это цвет радости и счастья!")
else:
    print("Это тоже хороший цвет!")
