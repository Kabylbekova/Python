

# str = ''
# list = []
# set = {}
# tuple = ()




# thistuple = ("apple",)
# print(type(thistuple))



# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])


# count()
# index()



# dict - словарь

# # set = {1, 2, 3, True}

# dict = {"one" : 1, "two":2}
# print(dict)

# Получить список ключей:

# x = thisdict.keys()


# Получите список значений:

# x = thisdict.values()

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change


# Метод items()вернет каждый элемент словаря в виде кортежей в списке.

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change


# # Чтобы определить, присутствует ли указанный ключ в словаре, используйте inключевое слово:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")







# dict = {
#         "имя": "Эрбол",
#         "Возраст" : 15,
#         "пол" : "мужчина"
#         }
# print(dict)



# numbers = {1: 'Один', 2: 'Два', 3: 'Три', 100: 'сто'}
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))


# goods = {
#      "apple": {"name": "Яблоки", "cost": 25, "kg": 30},
#      "pear": {"name": "Груши", "cost": 50, "kg": 5},
#      "plum": {"name": "Сливы", "cost": 55, "kg": 25},
#      "cherry": {"name": "Вишни", "cost": 110, "kg": 15}
# } 
# for item in goods.values():
#     if item["cost"] <= 100 and item["kg"] >= 10:
#         print(item["name"])





a, b ={1, 2, 3}, {3, 2, 1}
print(a==b, a is b)
