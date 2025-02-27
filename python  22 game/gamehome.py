import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень, ножницы, бумага")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифты
font = pygame.font.Font(None, 36)

# Варианты выбора
options = ["Камень", "Ножницы", "Бумага"]

# Создание временных изображений
rock_img = pygame.Surface((100, 100))
rock_img.fill((128, 128, 128))  # Серый цвет
scissors_img = pygame.Surface((100, 100))
scissors_img.fill((255, 0, 0))  # Красный цвет
paper_img = pygame.Surface((100, 100))
paper_img.fill((0, 255, 0))  # Зеленый цвет

images = {"Камень": rock_img, "Ножницы": scissors_img, "Бумага": paper_img}

# Функция для отображения текста

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    running = True

    user_choice = None
    computer_choice = None
    result = ""

    while running:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Проверка выбора игрока
                if 50 < x < 150 and 250 < y < 350:
                    user_choice = "Камень"
                elif 250 < x < 350 and 250 < y < 350:
                    user_choice = "Ножницы"
                elif 450 < x < 550 and 250 < y < 350:
                    user_choice = "Бумага"

                if user_choice:
                    computer_choice = random.choice(options)

                    # Определение результата
                    if user_choice == computer_choice:
                        result = "Ничья!"
                    elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
                         (user_choice == "Ножницы" and computer_choice == "Бумага") or \
                         (user_choice == "Бумага" and computer_choice == "Камень"):
                        result = "Вы победили!"
                    else:
                        result = "Компьютер победил!"

        # Отображение текста
        draw_text("Выберите: Камень, Ножницы, или Бумага", 100, 50)

        # Отображение кнопок
        pygame.draw.rect(screen, GRAY, (50, 250, 100, 100))
        pygame.draw.rect(screen, GRAY, (250, 250, 100, 100))
        pygame.draw.rect(screen, GRAY, (450, 250, 100, 100))
        
        screen.blit(images["Камень"], (50, 250))
        screen.blit(images["Ножницы"], (250, 250))
        screen.blit(images["Бумага"], (450, 250))

        # Если игрок сделал выбор, показать результаты
        if user_choice:
            draw_text(f"Ваш выбор: {user_choice}", 50, 150)
            draw_text(f"Выбор компьютера: {computer_choice}", 50, 200)
            draw_text(result, 50, 100, color=(0, 128, 0))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()