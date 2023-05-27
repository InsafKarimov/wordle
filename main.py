import random

# открываем файл
with open('words.txt', 'r', encoding='utf-8') as file:
    words = file.read().splitlines()

# выбираем случайное слово из файла
word = random.choice(words)

print("Угадайте слово!")

guesses = ''

# устанавливаем количество попыток
turns = 12

# подсчитываем неудачные попытки
while turns > 0:

    failed = 0

    for char in word:

        # сравниваем введенную букву с буквами в слове
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")

            # при ошибке увеличиваем на 1
            failed += 1

    if failed == 0:
        # мы выиграем, если кол-во проигрышов равно 0
        # и вывелась надпись, что мы выиграли
        print("Вы выиграли!")

        # выводим правильное слово
        print("Правильное слово: ", word)
        break

    print()
    guess = input("Введите букву:")

    # каждый введенный символ будет храниться в догадках
    guesses += guess

    # проверка ввода с символом в слове
    if guess not in word:

        turns -= 1

        # если буквы нет в слове, то выведется
        print("Неправильно!")

        # выводим, сколько осталось попыток
        print("Осталось попыток: ", + turns)

        if turns == 0:
            print("Вы проиграли!")
