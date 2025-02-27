

# x = int(input("enter x: "))
# y = int(input("enter y: "))
# def fun(x, y):
#     return x, y
# n = fun(x, y)
# print(n)


# def infoage_name(**name):
#     return name
# n2 = infoage_name(name='Asan')
# print(n2)



# def sum_numbers(*args):
#     return sum(args)
# print (sum_numbers(1, 2, 3, 4))



# def example_function(*args):
#     return print(args)
# ex = example_function(12,25, "asan")
# print(ex)




# def sum_numbers(*args):
#     return sum(args)  #*args-это кортеж-tuple
#     print(f"Summa: {result}")
#     return result
# s = sum_numbers(1, 2, 3, 4)
# print(s)

# numbers = [1, 2, 3, 4]
# print(sum_numbers(*numbers))





# def example_function(**kwargs):
#     return kwargs
# ex = example_function()
# print(ex)


# def print_user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
        
# res = print_user_info(name="Asan", age = 25, city= "Moskva")



# def sum_numbers(*args):
#     return sum(args)  #*args-это кортеж-tuple
#     print(f"Summa: {result}")
#     return result
# numbers = [1, 2, 3,44]
# print(sum_numbers(*numbers))




# def all_arguments(a, b, *args, c = 10, **kwargs):
#     resulat = f"a : {a} b : {b}, args : {args}, c : {c}, kwargs : {kwargs} "
#     return resulat 
# res = all_arguments(1, 2, 3, 4, 5, name="Ivan", city="moskva")
# print(res)




# args = (1, 2, 3 , 4)
# kwargs = {"d": 4, "e":5}
# c = 15
# d = 25
# b = 16

# def example(*a, b, c, d, **e):
#     print(a, b, c, d, e)
# example(*args, **kwargs)





# args = (1, 2, 3, 4)
# kwargs = {"e": 5, "f": 6}
# c = 15
# d = 25
# b = 16

# def example(*a, b, c, d, **e):
#     return a, b, c, d, e

# # Передаем явные значения для b, c, d, так как они обязательны
# result = example(*args, b=b, c=c, d=d, **kwargs)
# print(result)




"""                                    ДЗ                                                     """


# def numbers(*args):
#     result = 1  
#     for num in args:
#         result *= num  
#     return result

# print(numbers(2, 3, 4)) 





# def user(name, age, profession, city):
#     return f"{name}, {age} лет, {profession}, живет в {city}"

# name = input('Введите свое имя: ').title()
# age = int(input('Введите свой возраст: '))
# profession  = input('Введите профессию: ')
# city = input('Где вы живете: ').title()
# print(user(name, age, profession, city))







# def filter_numbers(*args):
#     res = [arg for arg in args if isinstance(arg, (int, float))]
#     return res

# filters = filter_numbers(2,43,54,5,5657,46456.6456, 5464,4646,'Hello-World','Aijan')

# print(filters)








