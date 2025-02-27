


# 1

from functools import reduce

# num = [14, 15, 47, 25]
# number = reduce(lambda x, y: x + y, num)
# print(number)


# 2
from functools import reduce

# # Функция-обработчик: складывает два числа
# def add(x, y):
#     return x + y

# numbers = [1, 2, 3, 4]
# result = reduce(add, numbers)
# print(result)  


# 3

# num = []
# res = reduce(lambda x, y: x + y, num, 0)    # 0 — начальное значение
# print(res)

# 4

# numbers = [1, 2, 3, 4, 5]

# # filter возвращает итератор
# result = filter(lambda x: x % 2 == 0, numbers)

# print(result)  # Вывод: <filter object>
# print(list(result))  # Вывод: [2, 4]


# # 5

# numbers = [0, 1, 2, "", None, 3]

# # Вместо лямбда-функции используем встроенную функцию bool
# result = filter(bool, numbers)
# print(list(result))  


# 6


# Допустим, вам нужно оставить только чётные числа и увеличить их на 1.
# filter не умеет одновременно преобразовывать данные.
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)  # Можно только отфильтровать
# Преобразование (увеличение на 1) нужно делать отдельно


# 7


# from functools import reduce

# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)  # Вывод: 10


# numbers = [1, 2, 3, 4]
# result = 0
# for num in numbers:
#     result += num
# print(result) 


# # 8

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique = (x for x in numbers if numbers.count(x) == 1)
# print(list(unique))
    
    
    # 9
    
# num = []
# number = list(filter(lambda x : x % 2 == 0, num))
# print(number)

# num = []
# number = reduce(lambda x, y: x + y, num)
# print(number)

# filter на пустом списке просто вернёт пустой итератор.
# reduce вызовет ошибку на пустом списке без начального значения, но если начальное значение указано, оно будет результатом.


# 10


# from collections import Counter

# numbers = [1, 2, 2, 3, 4, 4, 5]
# counter = Counter(numbers)

# # Выбираем только те элементы, которые встречаются больше одного раза
# repeated = [num for num, count in counter.items() if count > 1]
# print(repeated) 


# 11

# from functools import reduce

# strings = ["Hello", " ", "World", "!"]

# # Конкатенация строк
# result = reduce(lambda x, y: x + y, strings)
# print(result)  # Вывод: Hello World!


# 12

# numbers = [1, 2, 3, 4, 5]
# filtered = filter(lambda x: x % 2 == 0, numbers)
# print(list(filtered))  


# 13


# number = [10, 1, 2, 5, 5, 9]
# num = reduce(lambda x, y : x * y, number )
# print(num)


# 14


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# num_fil = filter(lambda x: x % 2 == 0, numbers)

# # print(list(num_fil))
# num_red = reduce(lambda x, y: x * y, num_fil)
# print( num_red)


# 15

# numbers = [1, 2, 3, 4, 5, 6]

# # Сначала фильтруем чётные числа, затем умножаем их на 10
# result = map(lambda x: x * 10, filter(lambda x: x % 2 == 0, numbers))

# print(list(result)) 



# 16


# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]

# zipped = zip(names, ages)
# print(list(zipped))  


# 17


# numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # reverse =True для убывание


# 18

# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)


# # 19

# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Шаг 1: Отбираем нечётные числа
# odd_numbers = filter(lambda x: x % 2 != 0, numbers)

# # Шаг 2: Находим максимальное нечётное число
# max_odd = reduce(lambda x, y: x if x > y else y, odd_numbers)

# print(max_odd) 




