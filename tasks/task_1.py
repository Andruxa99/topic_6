name_pet: str = input("Введите имя вашего питомца: ")

# Первый вариант решения
if name_pet == "Барсик" or name_pet == "Мурка":
    print("У вас классное имя для питомца!")
else:
    print("Это тоже хорошее имя для питомца!")

# Второй вариант решения
name_pet_2 = ("У вас классное имя для питомца!"
              if name_pet == "Барсик" or name_pet == "Мурка"
              else "Это тоже хорошее имя для питомца!")
print(name_pet_2)
