


### *Что такое алгоритм?*

'''
*Алгоритм* — это точная последовательность действий или инструкций,
 предназначенная для решения задачи или достижения конкретного результата. 

Алгоритмы можно сравнить с кулинарным рецептом: они дают пошаговые указания, 
чтобы получить ожидаемый результат.
'''

### *Основные свойства алгоритмов*
'''
1. *Дискретность*  
   Алгоритм состоит из отдельных шагов или действий,
     выполняемых последовательно.

2. *Понятность*  
   Каждый шаг алгоритма должен быть четко определен и понятен 
   для выполнения.

3. *Конечность*  
   Алгоритм всегда должен завершаться через конечное количество шагов.

4. *Определённость*  
   Один и тот же входной набор данных всегда даёт один и тот же результат.

5. *Результативность*  
   Алгоритм обязательно должен приводить к решению задачи или 
   к чётко определённому результату.
'''

# #### *1. Дискретность*  
# Каждый шаг алгоритма выполняется последовательно
#  и не пересекается с другими.  
# *Пример: Расчет суммы чисел.*


def calculate_sum(numbers):
    total = 0  # Шаг 1: Инициализация суммы
    for num in numbers:  # Шаг 2: Проход по каждому числу
        total += num  # Шаг 3: Добавление числа к сумме
    return total  # Шаг 4: Возврат результата

# Пример использования
numbers = [1, 2, 3, 4, 5]
print("Сумма чисел:", calculate_sum(numbers))  # Ожидаемый результат: 15


# #### *2. Понятность*  
# Каждый шаг алгоритма четко определен и понятен.  
# *Пример: Проверка, является ли число четным.*

def is_even(number):
    # Шаг 1: Проверить остаток от деления числа на 2
    if number % 2 == 0:
        res = number 
    return res

 # Шаг 2: Вернуть True, если остаток равен 0, иначе False

# Пример использования
print("Число 4 четное?", is_even(4))  # Ожидаемый результат: True
print("Число 5 четное?", is_even(5))  # Ожидаемый результат: False


# #### *3. Конечность*  
# Алгоритм всегда завершится после выполнения заданного
#  количества шагов.  
# *Пример: Нахождение максимального числа в списке.*
def find_max(numbers):
    max_number = numbers[0]  # Шаг 1: Предположим, что первый элемент максимальный
    for num in numbers:  # Шаг 2: Перебираем элементы списка
        if num > max_number:  # Шаг 3: Если текущий элемент больше
            max_number = num  # Шаг 4: Обновляем максимум
    return max_number  # Шаг 5: Возвращаем максимальное число

numbers = [10, 20, 5, 30, 25]
# {2,35,5,4}
# (24,4,354,6)
# range(11)
# range(1,101)
# range(1,10,2)
print("Максимальное число:", find_max(numbers))  # Ожидаемый результат: 30


# #### *4. Определённость*  
# На одинаковых входных данных алгоритм всегда выдаёт
#  один и тот же результат. 
#  
# *Пример: Сортировка списка.*


def sort_list(numbers):
    return sorted(numbers)  # Шаг 1: Используем встроенную функцию для сортировки

# Пример использования
numbers = [3, 1, 4, 1, 5, 9]
print("Отсортированный список:", sort_list(numbers))  # Ожидаемый результат: [1, 1, 3, 4, 5, 9]


# #### *5. Результативность*  
# Алгоритм обязательно приводит к решению задачи.  
# *Пример: Подсчет количества слов в тексте.*

def count_words(text):
    words = text.split()  # Шаг 1: Разбиваем текст на слова
    return len(words)  # Шаг 2: Возвращаем количество слов

# Пример использования
text = "Алгоритмы помогают решать задачи эффективно"
print("Количество слов:", count_words(text))  # Ожидаемый результат: 5

### *Зачем нужны алгоритмы?*
'''
1. *Автоматизация задач*  
   Алгоритмы позволяют автоматизировать процессы, 
   исключая необходимость ручного выполнения задач.

2. *Оптимизация времени*  
   Эффективные алгоритмы позволяют решать задачи быстрее
     и с минимальными затратами ресурсов.

3. *Решение сложных задач*  
   Некоторые задачи слишком сложны для человека, 
   но алгоритмы помогают разбить их на более простые этапы.

4. *Построение программ*  
   Любая компьютерная программа основывается на алгоритмах,
     определяющих её работу.
'''


### *Когда использовать алгоритмы?*
'''
- *При решении задач, требующих последовательных действий.*  
  Например, сортировка списка, поиск элемента, вычисление значения.

- *Для работы с большими объёмами данных.*  
  Оптимальные алгоритмы ускоряют обработку информации.

- *При необходимости автоматизации рутинных задач.*  
  Например, рассылка писем, расчет зарплаты, обработка платежей.

- *Для анализа данных и машинного обучения.*  
  Алгоритмы анализируют большие наборы данных, находят закономерности и делают прогнозы.
'''


### *Примеры использования алгоритмов в жизни*

'''
1. *Навигация*  
   GPS использует алгоритмы поиска кратчайшего пути (например, алгоритм Дейкстры).

2. *Сортировка данных*  
   Интернет-магазины сортируют товары по цене, популярности и другим критериям с помощью алгоритмов сортировки.

3. *Поиск информации*  
   Поисковые системы, такие как Google, используют сложные алгоритмы для выдачи наиболее релевантных результатов.

4. *Шифрование и безопасность*  
   Алгоритмы обеспечивают защиту данных, например, в банковских системах.

'''

### *Классификация алгоритмов*

'''1. *По структуре:*
   - Линейные (последовательные шаги).
   - Ветвящиеся (с условными операторами).
   - Циклические (повторяющиеся действия).

2. *По способу выполнения:*
   - Итеративные (с использованием циклов).
   - Рекурсивные (вызывают сами себя).

3. *По задаче:*
   - Сортировка (например, пузырьковая сортировка).
   - Поиск (например, бинарный поиск).
   - Шифрование (например, алгоритм RSA).

'''

### *Пример применения алгоритма*
# *Задача:* Найти среднее значение чисел в списке.  

# Алгоритм:  
# 1. Сложить все числа.  
# 2. Подсчитать количество чисел.  
# 3. Разделить сумму на количество.  



# Алгоритм нахождения среднего значения
def average(numbers):
    total = sum(numbers)  # Сумма всех чисел
    count = len(numbers)  # Количество чисел
    return total / count  # Среднее значение

# Пример
numbers = [10, 20, 30, 40, 50]
print("Среднее значение:", average(numbers))

'''
Алгоритмы — это фундаментальная основа программирования и компьютерных наук.
 Их понимание и умение применять — ключ к созданию эффективных программ!'''


# 1. *Линейный алгоритм*  
#    Пример: вычисление среднего значения чисел в списке.


# Функция вычисления среднего значения
def average(numbers):
    # Суммируем все числа в списке
    total = sum(numbers)  # Пример: [10, 20, 30] -> 60
    # Считаем количество чисел в списке
    count = len(numbers)  # Пример: [10, 20, 30] -> 3
    # Возвращаем результат деления суммы на количество
    return total / count  # Пример: 60 / 3 -> 20

# Пример использования
numbers = [10, 20, 30, 40, 50]
print("Среднее значение:", average(numbers))  # Ожидаемый результат: 30.0


# 2. *Циклический алгоритм*  
#    Пример: нахождение суммы всех четных чисел в списке.


# Функция нахождения суммы четных чисел
def sum_of_evens(numbers):
    total = 0  # Переменная для хранения суммы
    for num in numbers:  # Перебираем каждый элемент списка
        if num % 2 == 0:  # Проверяем, является ли число четным
            total += num  # Если четное, добавляем к сумме
    return total  # Возвращаем итоговую сумму

# Пример использования
numbers = [1, 2, 3, 4, 5, 6]
print("Сумма четных чисел:", sum_of_evens(numbers))  # Ожидаемый результат: 12


# 3. *Рекурсивный алгоритм*  
#    Пример: нахождение факториала числа.


# Функция нахождения факториала числа
def factorial(n):
    # Базовый случай: факториал 0 или 1 равен 1
    if n == 0 or n == 1:
        return 1
    # Рекурсивный вызов: n * факториал (n-1)
    return n * factorial(n - 1)

# Пример использования
print("Факториал 5:", factorial(5))  # Ожидаемый результат: 120


# 4. *Алгоритм сортировки*  
#    Пример: пузырьковая сортировка списка чисел.


# Функция пузырьковой сортировки
def bubble_sort(numbers):
    n = len(numbers)  # Количество элементов в списке
    for i in range(n):
        for j in range(0, n - i - 1):  # Сравниваем элементы попарно
            if numbers[j] > numbers[j + 1]:  # Если текущий больше следующего
                # Меняем местами элементы
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers  # Возвращаем отсортированный список

# Пример использования
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Отсортированный список:", bubble_sort(numbers))  # Ожидаемый результат: [11, 12, 22, 25, 34, 64, 90]


# 5. *Поиск элемента в списке*  
#    Пример: бинарный поиск.


# Функция бинарного поиска
def binary_search(numbers, target):
    low = 0  # Начальный индекс
    high = len(numbers) - 1  # Конечный индекс

    while low <= high:
        mid = (low + high) // 2  # Середина текущего диапазона
        if numbers[mid] == target:  # Если нашли элемент
            return mid  # Возвращаем индекс
        elif numbers[mid] < target:  # Если искомое больше середины
            low = mid + 1  # Сдвигаем начало диапазона
        else:  # Если искомое меньше середины
            high = mid - 1  # Сдвигаем конец диапазона

    return -1  # Если элемент не найден

# Пример использования
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print("Индекс элемента:", binary_search(numbers, target))  # Ожидаемый результат: 3


### *Пример использования алгоритмов*

'''Алгоритмы можно объяснить на примерах из повседневной жизни или программирования. 
Ниже приведен простой пример алгоритма для нахождения минимального числа в списке.

'''
### *Что такое алгоритм?*

'''*Алгоритм* — это последовательность шагов, которую необходимо выполнить для решения задачи.  

*Пример задачи:* Найти минимальное число в списке.  
'''

### *Код:*


# Функция для нахождения минимального числа в списке
def find_minimum(numbers):
    # Шаг 1: Предполагаем, что первый элемент минимальный
    minimum = numbers[0]
    
    # Шаг 2: Проходим по всем элементам списка
    for num in numbers:
        # Шаг 3: Если текущий элемент меньше минимального, обновляем минимальное значение
        if num < minimum:
            minimum = num
    
    # Шаг 4: Возвращаем минимальное значение
    return minimum

# Пример использования функции
numbers = [15, 8, 22, 3, 7, 9]
print("Минимальное число:", find_minimum(numbers))  # Ожидаемый результат: 3



### *Пошаговое объяснение:*

# 1. *Инициализация минимального значения.*  
#    Предполагаем, что первый элемент списка — самый маленький.

# 2. *Перебор списка.*  
#    Сравниваем каждый элемент списка с текущим минимальным значением.

# 3. *Обновление минимального значения.*  
#    Если находим элемент меньше текущего минимума, обновляем значение.

# 4. *Возврат результата.*  
#    После завершения цикла возвращаем минимальное число.


### *Преимущества алгоритмов*
'''
- Простота и ясность действий.  
- Возможность автоматизации решения задачи.  
- Универсальность: работает для любого списка чисел.  
'''
### *Результат выполнения:*

# Минимальное число: 3









