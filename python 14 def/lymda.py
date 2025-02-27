# лямбда выражения 
# в питон это способ создания анонимных (безимянных) функций  которые могут быть использованы 
# там где ожидается функция но создание полноценной функции деф кажется лишним



# лямда функция это небольшая анонимная функция которую можно обьявить прямо в вырожении 
# она используется для выполнения простых операций 





# speak = input('Enter: ')
# def cat_says(speak):
#     speakcat = f'speak cat  {speak}  Mяу'
#     return speakcat
# cat = cat_says(speak)
# print(cat)





# while True:
#     try:
#         # Ввод данных
#         number = int(input('Введите первое число: '))
#         number1 = int(input('Введите второе число: '))
#         operation = input('Введите операцию (+, -, *, //): ')

#         # Определение лямбда-функций для арифметических операций
#         add = lambda x, y: x + y
#         minus = lambda x, y: x - y
#         multiply = lambda x, y: x * y
#         divide = lambda x, y: x // y

#         # Выбор операции
#         if operation == '+':
#             result = add(number, number1)
#         elif operation == '-':
#             result = minus(number, number1)
#         elif operation == '*':
#             result = multiply(number, number1)
#         elif operation == '//':
#             # Проверка деления на ноль
#             if number1 == 0:
#                 raise ZeroDivisionError
#             result = divide(number, number1)
#         else:
#             result = 'Некорректная операция!'

#         # Вывод результата
#         print(f'Результат: {result}')
    
#     except ZeroDivisionError:
#         print('Ошибка: деление на ноль невозможно!')
    
#     except ValueError:
#         print('Ошибка: введите корректное число!')

#     # Возможность выхода из цикла
#     should_continue = input("Хотите продолжить? (да/нет): ").strip().lower()
#     if should_continue != 'да':
#         print("Спасибо за использование программы!")
#         break




# def swap_case(word):
#     return word.swapcase()

# in_word = input('Ввеидте слово: ')
# result = swap_case(in_word)
# print(result)





# def echo(word, times):
#     return (word + ' ')* times

# word = input('Введите слово: ') 
# times = int(input('Сколько раз нужно повторить? '))
# result = echo(word, times)
# print(result)




# def best_friend_number(number):
#     return number * 2 + 10

# number = int(input('Введите число: '))
# result = best_friend_number(number)
# print(result)



# def is_duck(animal):
#     return animal.lower == 'утка'
# animal = input('Введите название животного:  ')
# if animal == 'утка':
#     print(True)
# else:
#     print(False)


# def add_exclamation(word):
#     return word + '!'
# word = input('Напиши слово ')
# result = add_exclamation(word) 
# print(result)



# def secret_code(word):
#     return word.replace('a', '@').replace('o', '0')

# word = input('Введите слово:  ')
# print(f'Cлово {secret_code(word)}')



# def banana_count(word):
#     return word.count('a')

# word = input('Введите слово:  ')
# print(f' {banana_count(word)}')



# def opposite_day(statement):
#     return not statement

# print(opposite_day(True))  # False
# print(opposite_day(False))  # True



# def translator(word):
#     return word.replace('р', 'л').replace('Р', 'Л')


# print(translator("программирование"))  
# print(translator("Ракета"))           



# # 1. Функция swap_case
# swap_case = lambda word: word.swapcase()
# in_word = input('Введите слово: ')
# print(swap_case(in_word))

# # 2. Функция echo
# echo = lambda word, times: (word + ' ') * times
# word = input('Введите слово: ') 
# times = int(input('Сколько раз нужно повторить? '))
# print(echo(word, times))

# # 3. Функция best_friend_number
# best_friend_number = lambda number: number * 2 + 10
# number = int(input('Введите число: '))
# print(best_friend_number(number))

# # 4. Функция is_duck
# is_duck = lambda animal: animal.lower() == 'утка'
# animal = input('Введите название животного:  ')
# print(is_duck(animal))

# # 5. Функция add_exclamation
# add_exclamation = lambda word: word + '!'
# word = input('Напиши слово: ')
# print(add_exclamation(word))

# # 6. Функция secret_code
# secret_code = lambda word: word.replace('a', '@').replace('o', '0')
# word = input('Введите слово:  ')
# print(f'Cлово {secret_code(word)}')

# # 7. Функция banana_count
# banana_count = lambda word: word.count('a')
# word = input('Введите слово:  ')
# print(f'Количество букв "а": {banana_count(word)}')

# # 8. Функция opposite_day
# opposite_day = lambda statement: not statement
# print(opposite_day(True))  # False
# print(opposite_day(False))  # True

# # 9. Функция translator
# translator = lambda word: word.replace('р', 'л').replace('Р', 'Л')
# print(translator("программирование"))  
# print(translator("Ракета"))









#1 сумма двух чисел

# summa = lambda a, b: a + b  
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# print(f'Summa: {summa(a, b)}')  


# 2 четный нечетный


# number = lambda a: 'Четное' if a % 2 == 0 else 'нечетное'
# a = int(input('Enter number: '))
# print(f'Число {a}-{number(a)}')

#3  квадрат числа\
    
# number = lambda a: a ** 2
# a = int(input('Enter number: '))
# print(number(a))



# 4 последняя буква строки

# word = lambda last : last[-1]  
# last = "Burul"
# print(word(last))


# 5 конкатенция

# plus = lambda pl ,rl : pl + ' '+ rl
# pl = 'Kabylbekova'
# rl = 'Burul'
# print(plus(pl, rl))

# # 6 сравнение 

# compare_apples_oranges = lambda apples, oranges : 'Больше яблок' if apples > oranges else 'Больше апельсинов ' if oranges > apples else 'ровно'
# apples = int(input('Введите чило яблок: '))
# oranges = int(input('Введите число апельсинов: '))
# print(compare_apples_oranges(apples,oranges))\
    
# # 7 Имя
# make_secret_name = lambda first_name, last_name: first_name[:3] + last_name[:3]
# last_name = input('Введите имя: ')
# first_name = input('Введите фамилию: ')
# print(make_secret_name(last_name, first_name))


# 8 зеркальное

# mirror_word= lambda word: word + word[::-1]
# word = input('Введите слово: ')
# print(mirror_word(word))


# 9 число строка

# is_number = lambda value: 'True' if value.isdigit() else 'False'

# value = input('Введите число или строку: ')
# print(is_number(value))

# 10 длинное слово

# longer_word = lambda word1, word2: word1 if len(word1) > len(word2) else word2
# word1 = input('enter word: ')
# word2 = input('enter word: ')
# print(longer_word(word1,word2))

# 11 ЗАГЛАВНЫЕ БУКВЫ

# make_loud = lambda word: word.upper()
# word = input('enter word: ')
# print(make_loud(word))


# 12 приветствия

# magical_greeting = lambda name: name
# name = input('enter your name: ')
# print(f'Привет, {magical_greeting(name)}, добро пожаловать в мир магии!')


# 13
# legs_count = lambda cats, dogs, spiders: (cats * 4) + (dogs * 4) + (spiders * 8)

# # Ввод данных
# cats = int(input("Введите количество кошек: "))
# dogs = int(input("Введите количество собак: "))
# spiders = int(input("Введите количество пауков: "))

# # Вывод результата
# print(f"Общее количество ног: {legs_count(cats, dogs, spiders)}")




# # 14 pizza

# is_pizza = lambda food: 'True' if food == 'pizza' else "false"
# food = input('enter word: ')
# print(is_pizza(food))


