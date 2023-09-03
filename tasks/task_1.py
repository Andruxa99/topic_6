name_pet: str = input("Введите имя вашего питомца: ")  # пользовательский ввод
name_pet2 = "Барсик" or "Мурка" if name_pet == "" \
    else "Это тоже хорошее имя для питомца!"
print(name_pet2)
