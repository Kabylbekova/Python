

# def info_name(*args, **kwargs):
#     full_name = " ".join(args) 
#     surname = kwargs.get("surname", "Фамилия не указана")  
#     return f"Full Name: {full_name}, Фамилия: {surname}"

# x = input("Enter name: ").title()
# y = input("Enter surname: ").title()

# print(info_name(x, surname=y))




"""Задание 1: Сумма чисел  
Напишите функцию, которая принимает любое количество чисел через *args и возвращает их сумму.  
"""
# def sum_args(*args):
#     return sum(args)

# number = input('Введите числа: ')
# args = map(int, number.split()) 
# print("Сумма чисел:", sum_args(*args))



""" Задание 2: Приветствие  
Создайте функцию, которая принимает любое количество имен через `*args` и печатает приветствие для каждого.  """


# def greet_people(*args):
#     for name in args:
#         print(f'Hello! {name}')
# greet_people('Asan', 'Alina','China','Vali')


"""Задание 3: Личные данные  
Напишите функцию, которая принимает **kwargs и выводит личные данные человека (например, имя, возраст, город).  
"""

# def personal_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}:{value}')
        
# personal_info(name = 'Ali', age = 18, city = "Bishkek")



'''Задание 4: Поиск максимума  
Создайте функцию, которая принимает любое количество чисел через `*args` и возвращает максимальное из них.  
'''

# def find_max(*args):
#     return max(args)
#     print(f'Максимум: {result}')
#     return result
# number = 1, 5, 6, 78, 110, 45, 555
# print(find_max(*number))





"""Задание 5: Соединение строк  
Напишите функцию, которая принимает любое количество строк через *args и возвращает их объединение через пробел.  

"""


# def join_strings(*args):
#     return ' '.join(args)

# result = join_strings('Hi','how ','are','you?')
# print(result)




"""Задание 6: Параметры запроса  
Создайте функцию, которая принимает `**kwargs`, имитируя параметры HTTP-запроса, и выводит их в формате:  
`ключ=значение`.  
"""


# def print_query_params(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}={value}")

# print_query_params(name="Alice", age=30, city="New York")



"""Задание 7: Фильтрация четных чисел  
Напишите функцию, которая принимает любое количество чисел через *args и возвращает список только четных чисел.  
"""
    

# def filter_even(*args):
#     return [num for num in args if num % 2 == 0]
# number = filter_even(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(number)



"""Задание 8: Динамическое умножение  
Напишите функцию, которая принимает обязательный параметр
`factor` через `**kwargs` и любое количество чисел через `*args`, 
умножая каждое число на `factor`.  
"""


# def multiply_by_factor(*args, **kwargs):
#     factor = kwargs.get('factor', 1)  
#     return [num * factor for num in args]

# result = multiply_by_factor(1, 2, 3, 4, factor=5)
# print(result)



"""Задание 9: Распаковка словаря  
Напишите функцию, которая принимает два аргумента: кортеж *args и словарь **kwargs. Выведите оба на экран.  
"""


# def unpack_and_print(*args, **kwargs):
#     print("Кортеж:", args)
#     print("Словарь:", kwargs)

# unpack_and_print(1, 2, 3, name="Alica", age=30)



""" Задание 10: Длина аргументов  
Создайте функцию, которая принимает любое 
количество аргументов через *args и **kwargs и возвращает их общее количество.  

"""


# def count_arguments(*args, **kwargs):
#     total = len(args) + len(kwargs)
#     return total
# print(count_arguments(1, 2, 3, name="Alice", age=30))


