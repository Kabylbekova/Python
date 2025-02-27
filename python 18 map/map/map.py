# map - это всторенная функция которая применяется для выполнения одной и
# той же операции к каждому элементу итерируемого обьекта списка кортежа

#   (), [], {}

# str, int - не работает

# map(function, iterable)

# function- функция которая юудет применяться к каждому элементу
# iterable - обьект элементы которго вы хотите обработать



# что делает мап
# функция принимает функцию и один или несколько списков 
# оно применяет функцию к каждому элементу списка и возвращает итератор 




# numbers = (1, 2, 3, 4, 5)
# def square(x):
#     return x**2
# square = map(square, numbers)
# print(list(square))



# numbers = (1, 2, 3, 4, 5)
# sum = map(lambda x: x ** 2, numbers)
# print(list(sum))





# # 1 
# num = [5, 10, 15]
# sum  = map(lambda x: x * 2, num)
# print(list(sum))

# # 2
# number = [1.1, 2.2, 3.3]
# res = (map(int, number))
# print(list(res))


# # 3
# number = [4, 6, 8]
# sum = map(lambda x: x +5, number)
# print(list(sum))


# # 4
# word = ["hello", "world"]
# word_up = map(lambda x: x.upper(), word)
# print(list(word_up))


# # 5
# num = [1, 3, 5]
# number  = map(lambda x: x ** 2, num)
# print(list(number))



# # 6
# num1 = [2, 4, 6]
# num2 = [3, 5, 7]
# numbers = map(lambda x, y: x * y, num1, num2)
# print(list(numbers))


# 7

# word =  ["cat", "dog"]
# word_len = map(lambda x: len(x), word)
# print(list(word_len))


# 8


# number = [8, 10, 12]
# sum = map(lambda x: x - 2, number)
# print(list(sum))


# # 9
# word = ["python", "java"]
# word_tit = list(map(lambda x: x.title(), word))
# print(word_tit)


# # 10
# num = [4, 9, 16]
# number = map(lambda x: x ** 0.5, num)
# print(list(number))


# # 11
# word = ["map", "lambda", "python"]
# word_len = map(lambda x: len(x), word)
# print(list(word_len))


# # 12
# word = ["apple", "banana"]
# word_len = map(lambda x: x [0], word)
# print(list(word_len))


# 13

# word1 = ["one", "two"] 
# word2 =  ["three", "four"]
# word_can = map(lambda x, y: x + " " + y, word1, word2)
# print(list(word_can))


# 14

# num = [10, 20, 30]
# number = map(lambda x: x % 3, num)
# print(list(number))


# # 15
# num = [2, 4, 6]
# number = map(lambda x: x ** 3, num)
# print(list(number))



# 16

# print(list(map(str, [12, 18, 24])))

# num = [12, 18, 24]
# strnum = tuple(map(str, num))
# print(strnum)

# 17
# print(list(map(lambda x: x[:3], ['abcd', 'gfjkg'])))

# 18

# print(list(map(lambda x: x.strip(), ['  hello   ', ' world '])))






""" cccccccccccccccccccccccccccccccc        Home work      ccccccccccccccccccccccccccccccccccccccccccccc """





# # 1
# number = [5, 10, 15]
# num = map(lambda x: x * 2, number)
# print(list(num))


# 2

# num = [1.1, 2.2, 3.3]
# number = map(lambda x: int(x), num)
# print(list(number))


# 3

# num = [4, 6, 8]
# number = map(lambda x: x + 5, num)
# print(list(number))

# 4

# word = ["hello", "world"]
# word_up = map(lambda x: x.upper(), word)
# print(list(word_up))


# 5

# num = [1, 3, 5]
# number = map(lambda x: x ** 2, num)
# print(list(number))



# 6

# num1 = [2, 4, 6] 
# num2 = [3, 5, 7]
# number = map(lambda x, y: x * y, num1, num2)
# print(list(number))


# 7

# word =  ["cat", "dog"]
# word_len = map(lambda x: len(x), word)
# print(list(word_len))


# 8

# num = [8, 10, 12]
# number = map(lambda x: x - 2, num)
# print(list(number))



# 9

# word = ["python", "java"]
# title_word = map(lambda x: x.title(), word)
# print(list(title_word))



# # 10

# num = (9, 16, 25)
# number = map(lambda x: x ** 0.5 , num)
# print(list(number))