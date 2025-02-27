# # number1 = int(input("enter number: "))
# # number2 = int(input("enter number: "))

# # def add(number1, number2):
# #     sumres = number1 + number2
# #     return f'summa numbers ->{sumres}'

# # a = add(number1, number2)
# # print(a)


# # Функция - именнованный бблок кода, который может принять аргументы и возвращать результат


# # def my_sum(x,y):
# #     return x+y

# # res= my_sum(5,6)
# # print('res',res)

# # def my_len(obj):
# #     count = 0
# #     for element in obj:
# #         count += 1
# #         return count
    
# # res = my_len(['abc', 1,2,3])
# # print(res)


# # list_  = ['abc', 1,2,3]
# # count = 0
# # for element in list_:
# #     count += 1
# # print(count)
# # str_ = 'abcde'
# # count = 0
# # for element in str_:
# #     count += 1 
# # print(count)


# # Функции соблюдают прицип DRY (dont reply yoerself)

# # параметры переменные внутри функции, значения которым мы задаем при вызове функции ()
# # аргументы значения которые мы передаем при вызове функции




# name = input('enter name: ')
# age = int(input('Enter age: '))
# def name_age_into():
#     resulat = f"name -> {name} age-> {age}"
#     return resulat 

# N = name_age_into()

# def name_age_into_a(name , age):
#     resulat = f'name -> {name} age-> {age}'
#     return resulat  

# na = name_age_into_a(name, age)

# print(N)
# print(na)





# a = int(input("Введите первое число:  "))
# b = int(input("Введите второе число:  "))
# s = input('Выберите -> +, -, *, **, /, // :  ')

# def calculator(a, b, s):
#     if s == '+':
#         resulat = a + b
#     elif s == '-':
#         resulat = a - b
#     elif s == '*':
#         resulat = a * b
#     elif s == '**':
#         resulat = a ** b
#     elif s == '/':
#         resulat = a / b
#     elif s == '//':
#         resulat = a // b
#     else:
#         print(f'Такого символа нет{s}')
#     return f'resulat numbers ->{resulat}'

# cal = calculator(a, b, s)
# print(cal)







# name = input('Enter name: ').title()
# age = int(input('Enter age: '))

# def name_age_info():
#     result = f"name -> {name} age -> {age}"
#     return result 

# N = name_age_info()
# print(N)





# def my_name(name, age):
#     return f"{name}, {age} years old"

# res = my_name("Burul", 18)
# print('Result:', res)






# Виды параметров

# обязательное, не обязательное , с деволтом (со значением оп умолчанию), 
# kwards (все лишние именованные аргументы)


# Виды аргументов 
# позиционные  по позиции
# именованные по названию (параметр значение)






# def find_minimum(a, b, c):
#     return min(a, b, c)

# print(find_minimum(3, 5, 2)) 
 
 
 
 
 
# def split_words(sentence):
#     return sentence.split()

# print(split_words("Привет мир это тест"))










