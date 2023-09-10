ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит:""\n"
      "1. Латинский" "\n"
      "2. Кириллица")

alphabet = int(input("Введите номер алфавита: "))
if alphabet >= 3:
    print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
user_input = input("Введите букву: ")
