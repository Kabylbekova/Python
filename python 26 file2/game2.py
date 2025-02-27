import random

# Файл для сохранения истории игр
FILE_NAME = "game_history.txt"

def write_to_file(mode, content):
    """Функция для записи данных в файл в заданном режиме."""
    with open(FILE_NAME, mode) as file:
        file.write(content + "\n")

def read_history():
    """Функция для чтения истории игр."""
    try:
        with open(FILE_NAME, "r") as file:
            print("История игр:")
            print(file.read())
    except FileNotFoundError:
        print("История еще не создана. Начните новую игру!")

def play_game():
    """Основная логика игры."""
    print("Добро пожаловать в игру 'Угадай число'!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            user_guess = int(input("Ваш вариант: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Мое число больше!")
            elif user_guess > number_to_guess:
                print("Мое число меньше!")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
                write_to_file("a", f"Число: {number_to_guess}, Попытки: {attempts}")
                break
        except ValueError:
            print("Введите целое число!")

def main():
    """Главное меню игры."""
    while True:
        print("\nВыберите действие:")
        print("1. Играть в игру")
        print("2. Посмотреть историю игр")
        print("3. Сбросить историю")
        print("4. Выйти")
        
        choice = input("Ваш выбор: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            read_history()
        elif choice == "3":
            try:
                with open(FILE_NAME, "w") as file:
                    pass  # Просто очистим файл
                print("История игр сброшена.")
            except FileNotFoundError:
                  print("Некорректный выбор. Попробуйте снова.")

# if __name__ == "__main__":
#     main()
