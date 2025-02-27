import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Цвета
BG_COLOR = (28, 170, 185)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)
TEXT_COLOR = (255, 255, 255)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-Нолики")
screen.fill(BG_COLOR)

# Шрифт для текста
font = pygame.font.Font(None, 50)

# Сетка игры
board = [[None for _ in range(3)] for _ in range(3)]

# Переменные игры
current_player = "X"
game_over = False
winner_text = ""

# Отрисовка линий сетки
def draw_lines():
    # Горизонтальные линии
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)
    # Вертикальные линии
    pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)

# Отрисовка крестиков и ноликов
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == "X":
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * WIDTH // 3 + SPACE, row * HEIGHT // 3 + SPACE), 
                                 (col * WIDTH // 3 + WIDTH // 3 - SPACE, row * HEIGHT // 3 + HEIGHT // 3 - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * WIDTH // 3 + SPACE, row * HEIGHT // 3 + HEIGHT // 3 - SPACE), 
                                 (col * WIDTH // 3 + WIDTH // 3 - SPACE, row * HEIGHT // 3 + SPACE), CROSS_WIDTH)

# Отображение сообщения о победителе
def display_winner(message):
    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()  # Обновление экрана

WINNING_COMBINATIONS = [
    [(0, 0), (0, 1), (0, 2)],  # Первая строка
    [(1, 0), (1, 1), (1, 2)],  # Вторая строка
    [(2, 0), (2, 1), (2, 2)],  # Третья строка
    [(0, 0), (1, 0), (2, 0)],  # Первый столбец
    [(0, 1), (1, 1), (2, 1)],  # Второй столбец
    [(0, 2), (1, 2), (2, 2)],  # Третий столбец
    [(0, 0), (1, 1), (2, 2)],  # Главная диагональ
    [(0, 2), (1, 1), (2, 0)],  # Обратная диагональ
]

def check_winner():
    global game_over, winner_text
    for combination in WINNING_COMBINATIONS:
        if all(board[row][col] == "X" for row, col in combination):
            game_over = True
            winner_text = "Победитель: X"
            return "X"
        if all(board[row][col] == "O" for row, col in combination):
            game_over = True
            winner_text = "Победитель: O"
            return "O"

    if all(all(row) for row in board):
        game_over = True
        winner_text = "Ничья"
        return "Ничья"

    return None

# Сброс игры
def restart_game():
    global board, current_player, game_over, winner_text
    board = [[None for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    winner_text = ""
    screen.fill(BG_COLOR)
    draw_lines()

# Ход компьютера
def computer_move():
    # Проверка на выигрышный ход
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = "O"
                if check_winner() == "O":
                    return
                board[row][col] = None

    # Блокировка игрока
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = "X"
                if check_winner() == "X":
                    board[row][col] = "O"
                    return
                board[row][col] = None

    # Выбор центральной клетки
    if board[1][1] is None:
        board[1][1] = "O"
        return

    # Ход в случайную клетку
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] is None]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

# Основной цикл
restart_game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_player == "X":
            mouseX = event.pos[0]  # координата X
            mouseY = event.pos[1]  # координата Y

            clicked_row = mouseY // (HEIGHT // 3)
            clicked_col = mouseX // (WIDTH // 3)

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = current_player
                draw_figures()
                winner = check_winner()
                if winner:
                    display_winner(winner_text)
                else:
                    current_player = "O"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    if current_player == "O" and not game_over:
        computer_move()
        draw_figures()
        winner = check_winner()
        if winner:
            display_winner(winner_text)
        else:
            current_player = "X"

    pygame.display.update()
