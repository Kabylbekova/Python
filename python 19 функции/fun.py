"""функция zip в питоне испльзуется для обьедения нескольких итерабельных обьектов списков кортежей строк и тд 
в один итератор который генерирет кортежи сосьоящие из элементов которые находятся на соответствующих 
позициях в каждом из переданных итераторов"""



# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c']
# res = zip(list1, list2)
# print(list(res))




# list_of_tuples = list(zip([1, 2], ['a', 'b']))
# print(list_of_tuples)




# zipped = [(1, 'a'), (2, 'b')]
# num, let =zip(*zipped)
# print(num)
# print(let)



"""" enumerate  возвращает итератор который генерирует кортежи где первый элемент это индекс элемента в итеруреом
обьекте а второй сам элемент можно указать начальный индекс по умолчанию 0 """


# lst = ['a', 'b', 'c']
# for index, value in enumerate(lst):
#     print(index, value)


# lis2 = ['Alina', 'Asan', 'Ali', 'Sezim']
# for num, name in enumerate(lis2, start=1):
#     print(num,'.', name)




# for index, value in enumerate(range(5)):
#     print(f'Index: {index}, value: {value}')


# list1 = [1, 2, 3, 4, 5]
# list2= ['a', 'b', 'c']
# list3 = [10.1, 11.5, 45.4, 45.7, ]
# zipped = zip(list1, list2, list3)
# for el in zipped:
#     print(el)




# list1 = [1, 2, 3, 4, 5]
# list2= ['a', 'b', 'c', 'f']
# dict_ = dict(zip(list1,list2))
# print(dict_)


# string = 'hello'
# enum = enumerate(string)
# for el in enum:
#     print(el)





""" _________________________---------------------------------------______________________"""

# 1, 2

# lst = ["a", "b", "c"]
# lst1 = [100, 200, 300]
# lst2 = [1, 2, 3]

# lst3 = zip(lst, lst2, lst1)
# print(list(lst3))


# 3

# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b']
# res = zip(list1, list2)
# print(list(res))


# 4


# name =  ["name", "age"]
# age = ["Alice", 25]
# res = dict(zip(name, age))
# print(res)


# 5

# string = "abc"
# num = [1, 2, 3]
# res = (list(zip(string, num)))
# print(res)



# 6


# zipped = [(1, 'a'), (2, 'b')]
# num, let =zip(*zipped)
# print(num)
# print(let)


# 7


# pairs = [(1, 2), (3, 4)]
# list1, list2 = zip(*pairs)
# list1 = list(list1)
# list2 = list(list2)

# print(list1) 
# print(list2)  


# # 8


# numbers = [1, 2, 3]
# pairs = list(zip(numbers, numbers))

# print(pairs) 


# 9


# numbers = [1, 2, 3]
# numbers2 = [4, 5, 6]
# pairs = list(zip(numbers, numbers2))

# print(pairs) 



# 10


# name =  ["name", "age"]
# age = [24 , 25]
# res = dict(zip(name, age))
# print(res)


# 11

# letters = ["a", "b", "c"]

# result = list(zip(letters))

# print(result)  

# 12

# names = ["Аня", "Борис", "Виктор"]
# ages = [25, 30, 35]

# messages = [f"{name}: {age}" for name, age in zip(names, ages)]

# print(messages) 


# 13

# letters = ["a", "b"]
# numbers = [1, 2]

# result = [*zip(letters, numbers)]

# print(result) 




# 14

# numbers = [1, 2, 3]
# numbers2 = (4, 5, 6)
# pairs = list(zip(numbers, numbers2))

# print(pairs) 


# 15


# num = [1, 2, 3]
# word = ('x', 'y', 'z')
# res = dict(zip(num, word))
# print(res)


# # 16
# list1 = []
# list2 = [1, 2, 3]

# result = list(zip(list1, list2))

# print(result) 




"""Enumerate"""

# # 1

# lst = [10, 20, 30]
# for index, value in enumerate(lst):
#     print(f"Index: {index}, Value: {value}")
    
# # 2
# lst = [10, 20, 30]
# for index, value in enumerate(lst, start=1):
#     print(f"Index: {index}, Value: {value}")

# # 3
# word = "hello"
# result = list(enumerate(word))
# print(result)

# # 4
# lst = ["a", "b", "c"]
# result = list(enumerate(lst))
# print(result)


# # 5
# lst = ["a", "b", "c"]
# result = [f"{index}: {value}" for index, value in enumerate(lst)]
# print(result)



# # 6

# lst = ["a", "b", "c"]
# for index, value in enumerate(lst):
#     if index == 2:
#         lst[index] = "z"
# print(lst)




# # 7
# lst = []
# result = list(enumerate(lst))
# print(result)

# # 8

# values = ["cat", "dog", "bird"]
# indexed_dict = {index: value for index, value in enumerate(values)}
# print(indexed_dict)

# # 9
# lst = [1, 2, 3, 4, 5]
# result = [index for index, value in enumerate(lst) if value % 2 == 0]
# print(result)


# # 10
# gen = (x for x in range(5))
# for index, value in enumerate(gen):
#     print(f"Index: {index}, Value: {value}")


# 11

# lst = ["cat", "dog", "bird"]
# result = [f"{index}: {value}" for index, value in enumerate(lst)]
# print(result)



# 12

# lst = [10, 20, 30, 40, 50]
# result = [value for index, value in enumerate(lst) if index % 2 == 0]
# print(result)



# # 13

# lst = [1, 2, -3, 4]
# result = next((index for index, value in enumerate(lst) if value < 0), None)
# print(result)


# 14

# s = {"cat", "dog", "bird"}
# result = list(enumerate(s))
# print(result)



# 15

# lst = [10, 20, 30]
# count = sum(1 for _ in enumerate(lst))
# print(count)



# 16

# lst = [10, 20, 30]
# result = [(index, value + 5) for index, value in enumerate(lst)]
# print(result)


# 17

# word = "hello"
# result = list(enumerate(word))
# print(result)



