# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint num = randint (LOWER LIMIT,UPPER LIMIT)
#

from random import randint

secret_number = randint(0, 1000)
attempts = 10
guess = None

print("Угадайте число от 0 до 1000 за 10 попыток")

for i in range(attempts):
    guess = int(input(f"Попытка {i + 1}: "))
    if guess == secret_number:
        print("Поздравляем, вы угадали число!")
        break
    elif guess < secret_number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")

if guess != secret_number:
    print(f"К сожалению, вы не угадали число. Загаданное число было {secret_number}")
