#Функция reduce
# 1. Функция reduce
'''
Функция reduce из модуля functools позволяет последовательно 
применять переданную функцию к элементам последовательности, 
сводя её к одному итоговому значению.  
Алгоритм работы:
Берутся два первых элемента последовательности.
К ним применяется переданная функция.
Результат применения функции комбинируется со следующим элементом,
 и так далее, пока не останется одно значение.
'''
'''
Последовательно применяет функцию к элементам списка,
 сводя его к одному результату.

'''

# 2. Функция filter
# Функция filter используется для фильтрации элементов 
# последовательности, оставляя только те, которые соответствуют 
# заданному условию (функции).




from functools import reduce

list_ = [1, 4, 3, 6, 10, 5]
product = reduce(lambda x, y: x * y, list_)
print(product)
# 3600 = 1 * 4 * 3 * 6 * 10 * 5

'''
Пример с объединением строки:
'''

string = "hello"
res = reduce(lambda x, y: x + "$" + y, string)
print(res)
# 'h$e$l$l$o'


'''Пример поиска минимума:
'''

list_ = [1, 2, -4, 6, -1, 9]
min_value = reduce(lambda x, y: x if x < y else y, list_)
print(min_value)
# -4
'''

примеров использования функции reduce из модуля functools


'''
### *1. Суммирование чисел*

from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)
# 10


### *2. Перемножение чисел*

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)
# 24


### *3. Наибольшее число в списке*

numbers = [10, 20, 5, 8]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)
# 20


### *4. Наименьшее число в списке*

numbers = [10, 20, 5, 8]
min_number = reduce(lambda x, y: x if x < y else y, numbers)
print(min_number)
# 5


### *5. Конкатенация строк*

words = ['Hello', 'world', 'Python']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)
# 'Hello world Python'


### *6. Подсчет произведения четных чисел*

numbers = [1, 2, 3, 4, 5, 6]
even_product = reduce(lambda x, y: x * y if y % 2 == 0 else x, numbers, 1)
print(even_product)
# 48


### *7. Вычисление факториала*

n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)
# 120


### *8. Объединение словаря*

dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
merged_dict = reduce(lambda x, y: {**x, **y}, dicts)
print(merged_dict)
# {'a': 1, 'b': 2, 'c': 3}


### *9. Сложение чисел с начальным значением*

numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)
# 16


### *10. Преобразование списка в строку*

chars = ['P', 'y', 't', 'h', 'o', 'n']
word = reduce(lambda x, y: x + y, chars)
print(word)
# 'Python'


### *11. Нахождение длины строки*

words = ['Python', 'is', 'fun']
total_length = reduce(lambda x, y: x + len(y), words, 0)
print(total_length)
# 10


### *12. Вычисление разности*

numbers = [10, 3, 2]
difference = reduce(lambda x, y: x - y, numbers)
print(difference)
# 5


### *13. Вычисление суммы квадратов*

numbers = [1, 2, 3, 4]
sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)
print(sum_of_squares)
# 30


### *14. Фильтрация максимума из списков*

lists = [[1, 2], [3, 4], [5, 6]]
max_element = reduce(lambda x, y: x + y, lists)
print(max_element)
# [1, 2, 3, 4, 5, 6]


### *15. Преобразование в список без дубликатов*

numbers = [1, 2, 2, 3, 3, 4]
unique = reduce(lambda x, y: x + [y] if y not in x else x, numbers, [])
print(unique)
# [1, 2, 3, 4]


### *16. Умножение всех чисел на 2*

numbers = [1, 2, 3]
result = reduce(lambda x, y: x + [y * 2], numbers, [])
print(result)
# [2, 4, 6]


### *17. Сортировка в обратном порядке*

numbers = [4, 2, 8, 5]
sorted_list = reduce(lambda x, y: [y] + x, numbers, [])
print(sorted_list)
# [5, 8, 2, 4]


### *18. Поиск суммы элементов с использованием сложной логики*

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + (y if y % 2 == 0 else 0), numbers, 0)
print(result)
# 6


### *19. Генерация словаря из списка кортежей*

pairs = [('a', 1), ('b', 2), ('c', 3)]
dictionary = reduce(lambda acc, pair: {**acc, pair[0]: pair[1]}, pairs, {})
print(dictionary)
# {'a': 1, 'b': 2, 'c': 3}


### *20. Генерация списка степеней*

numbers = [2, 3, 4]
powers = reduce(lambda x, y: x + [x[-1] * y] if x else [y], numbers, [])
print(powers)
# [2, 6, 24]



'===================================================================================='

# filter, reduce
#Функция filter
'''
Фильтрует последовательность, 
оставляя только элементы, удовлетворяющие условию.
'''

list_ = [3, -5, 0, 10, -34]
positive_numbers = filter(lambda x: x > 0, list_)
print(list(positive_numbers))
# [3, 10]


'''Фильтрация списка словарей:
'''

users = [
    {'name': 'Nazyl', 'age': 10},
    {'name': 'Masha', 'age': 4},
    {'name': 'Anonym', 'age': 25}
]

adults = filter(lambda user: user['age'] > 12, users)
print(list(adults))
# [{'name': 'Anonym', 'age': 25}]

# примеров использования функции filter в Python:

# *1. Фильтрация четных чисел*

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# [2, 4, 6]


# *2. Фильтрация строк длиной больше 3*

words = ['cat', 'house', 'dog', 'sun']
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)
# ['house']


# *3. Исключение отрицательных чисел*

values = [-1, 0, 5, -3, 10]
positive_numbers = list(filter(lambda x: x >= 0, values))
print(positive_numbers)
# [0, 5, 10]


# *4. Фильтрация пустых строк*

strings = ['hello', '', 'world', '', 'Python']
non_empty_strings = list(filter(None, strings))
print(non_empty_strings)
# ['hello', 'world', 'Python']


# *5. Фильтрация по определенному значению*

fruits = ['apple', 'banana', 'cherry', 'apple']
apples = list(filter(lambda x: x == 'apple', fruits))
print(apples)
# ['apple', 'apple']


# *6. Использование функции вместо lambda*

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)
# [2, 4]


# *7. Фильтрация слов, содержащих букву 'a'*

words = ['cat', 'dog', 'parrot', 'fish']
words_with_a = list(filter(lambda word: 'a' in word, words))
print(words_with_a)
# ['cat', 'parrot']


# *8. Удаление None из списка*

data = [None, 1, 2, None, 3, None]
filtered_data = list(filter(None, data))
print(filtered_data)
# [1, 2, 3]


# *9. Фильтрация чисел больше 10*

numbers = [5, 10, 15, 20]
greater_than_ten = list(filter(lambda x: x > 10, numbers))
print(greater_than_ten)
# [15, 20]


# *10. Фильтрация пользователей старше 18*

users = [{'name': 'Alice', 'age': 17}, {'name': 'Bob', 'age': 20}]
adults = list(filter(lambda user: user['age'] > 18, users))
print(adults)
# [{'name': 'Bob', 'age': 20}]


# *11. Фильтрация уникальных элементов*

items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(filter(lambda x: items.count(x) == 1, items))
print(unique_items)
# [1, 3, 5]


# *12. Фильтрация строк, начинающихся с буквы 'P'*

cities = ['Paris', 'Berlin', 'Prague', 'London']
p_cities = list(filter(lambda city: city.startswith('P'), cities))
print(p_cities)
# ['Paris', 'Prague']


# *13. Числа в диапазоне от 5 до 15*

numbers = [3, 5, 7, 10, 20]
in_range = list(filter(lambda x: 5 <= x <= 15, numbers))
print(in_range)
# [5, 7, 10]


# *14. Фильтрация заглавных букв*

letters = ['a', 'B', 'c', 'D']
uppercase_letters = list(filter(str.isupper, letters))
print(uppercase_letters)
# ['B', 'D']


# *15. Удаление пробельных строк*

lines = ['Hello', ' ', 'World', '', 'Python']
clean_lines = list(filter(lambda line: line.strip(), lines))
print(clean_lines)
# ['Hello', 'World', 'Python']


# *16. Фильтрация чисел, делящихся на 3*

numbers = [1, 3, 6, 8, 9]
divisible_by_three = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_three)
# [3, 6, 9]


# *17. Фильтрация пользователей с определенным именем*

users = [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Alice'}]
only_alices = list(filter(lambda user: user['name'] == 'Alice', users))
print(only_alices)
# [{'name': 'Alice'}, {'name': 'Alice'}]


# *18. Фильтрация целых чисел*

data = [1.1, 2, 3.5, 4]
integers = list(filter(lambda x: isinstance(x, int), data))
print(integers)
# [2, 4]


# *19. Отбор строк с определенной длиной*

words = ['one', 'three', 'four', 'seven']
three_letter_words = list(filter(lambda word: len(word) == 3, words))
print(three_letter_words)
# ['one']


# *20. Фильтрация по признаку четности индекса*

numbers = [10, 20, 30, 40]
even_index_numbers = list(filter(lambda x: numbers.index(x) % 2 == 0, numbers))
print(even_index_numbers)
# [10, 30]